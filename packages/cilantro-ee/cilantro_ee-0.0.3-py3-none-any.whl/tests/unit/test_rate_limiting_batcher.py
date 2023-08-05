from unittest import TestCase
from cilantro_ee.nodes.masternode.transaction_batcher import RateLimitingBatcher
from cilantro_ee.core.crypto.wallet import Wallet, _verify
from cilantro_ee.services.storage.state import NonceManager
from cilantro_ee.core.utils.transaction import TransactionBuilder, transaction_is_valid
from contracting import config
from cilantro_ee.core.messages.capnp_impl import capnp_struct as schemas
import os
import capnp

transaction_capnp = capnp.load(os.path.dirname(schemas.__file__) + '/transaction.capnp')

n = NonceManager()


class MockQueue:
    def __init__(self):
        self.q = []

    def get(self):
        return self.q.pop(0)

    def qsize(self):
        return len(self.q)


def make_good_tx(processor):
    w = Wallet()
    balances_key = '{}{}{}{}{}'.format('currency',
                                       config.INDEX_SEPARATOR,
                                       'balances',
                                       config.DELIMITER,
                                       w.verifying_key().hex())
    n.driver.set(balances_key, 500000)
    tx = TransactionBuilder(w.verifying_key(),
                            contract='currency',
                            function='transfer',
                            kwargs={'amount': 10, 'to': 'jeff'},
                            stamps=500000,
                            processor=processor,
                            nonce=0)

    tx.sign(w.signing_key())
    tx_bytes = tx.serialize()
    tx_struct = transaction_capnp.Transaction.from_bytes_packed(tx_bytes)
    return tx_struct


def make_bad_tx():
    w = Wallet()
    balances_key = '{}{}{}{}{}'.format('currency',
                                       config.INDEX_SEPARATOR,
                                       'balances',
                                       config.DELIMITER,
                                       w.verifying_key().hex())
    n.driver.set(balances_key, 500000)
    tx = TransactionBuilder(w.verifying_key(),
                            contract='currency',
                            function='transfer',
                            kwargs={'amount': 10, 'to': 'jeff'},
                            stamps=500000,
                            processor=b'\x00' * 32,
                            nonce=0)

    tx.sign(w.signing_key())
    tx_bytes = tx.serialize()
    tx_struct = transaction_capnp.Transaction.from_bytes_packed(tx_bytes)
    return tx_struct


class TestRateLimitingBatcher(TestCase):
    def test_add_batch_id_adds_properly(self):
        r = RateLimitingBatcher(
            queue=MockQueue(),
            wallet=Wallet(),
            sleep_interval=0,
            max_batch_size=1,
            max_txn_delay=1
        )

        r.add_batch_id('123')

        self.assertListEqual(r.sent_batch_ids, ['123'])
        self.assertEqual(r.num_batches_sent, 1)

    def test_adding_multiple_batches_adjusts_accordingly(self):
        r = RateLimitingBatcher(
            queue=MockQueue(),
            wallet=Wallet(),
            sleep_interval=0,
            max_batch_size=1,
            max_txn_delay=1
        )

        r.add_batch_id('123')

        self.assertListEqual(r.sent_batch_ids, ['123'])
        self.assertEqual(r.num_batches_sent, 1)

        r.add_batch_id('567')

        self.assertListEqual(r.sent_batch_ids, ['123', '567'])
        self.assertEqual(r.num_batches_sent, 2)

    def test_adding_same_batch_ids_acts_like(self):
        # TBD
        pass

    def test_ready_for_next_batch_batches_sent_greater_than_2_returns_false(self):
        queue = MockQueue()

        r = RateLimitingBatcher(
            queue=queue,
            wallet=Wallet(),
            sleep_interval=0,
            max_batch_size=1,
            max_txn_delay=1
        )

        r.num_batches_sent = 3

        self.assertFalse(r.ready_for_next_batch())
        self.assertEqual(r.txn_delay, 0)

    def test_ready_for_next_batch_batches_sent_greater_than_2_returns_false_and_increments_if_tx_exists(self):
        queue = MockQueue()
        queue.q.append('tx!')

        r = RateLimitingBatcher(
            queue=queue,
            wallet=Wallet(),
            sleep_interval=0,
            max_batch_size=1,
            max_txn_delay=1
        )

        r.num_batches_sent = 3

        self.assertFalse(r.ready_for_next_batch())
        self.assertEqual(r.txn_delay, 1)

    def test_ready_for_next_batch_less_than_2_num_batches_sent_1_q_greater_than_max_batches_returns_false_and_increments(self):
        queue = MockQueue()

        queue.q.extend(['1', '2'])

        r = RateLimitingBatcher(
            queue=queue,
            wallet=Wallet(),
            sleep_interval=0,
            max_batch_size=3,
            max_txn_delay=1
        )

        r.num_batches_sent = 1

        self.assertFalse(r.ready_for_next_batch())
        self.assertEqual(r.txn_delay, 1)

    def test_ready_for_next_batch_lt_2_num_batches_tx_delay_lt_max_txn_submission_delay_returns_false(self):
        queue = MockQueue()

        r = RateLimitingBatcher(
            queue=queue,
            wallet=Wallet(),
            sleep_interval=0,
            max_batch_size=3,
            max_txn_delay=1
        )

        r.num_batches_sent = 1

        self.assertFalse(r.ready_for_next_batch())
        self.assertEqual(r.txn_delay, 0)

    def test_ready_for_next_batch_lt_2_num_batches_tx_delay_lt_max_txn_submission_delay_returns_false_and_increments(self):
        queue = MockQueue()
        queue.q.extend(['1', '2'])

        r = RateLimitingBatcher(
            queue=queue,
            wallet=Wallet(),
            sleep_interval=0,
            max_batch_size=3,
            max_txn_delay=1
        )

        r.num_batches_sent = 1

        self.assertFalse(r.ready_for_next_batch())
        self.assertEqual(r.txn_delay, 1)

    def test_num_batches_lt_2_num_batches_sent_gt_0_and_q_gt_mx_batches_and_tx_delay_gt_max_delay_returns_true(self):
        queue = MockQueue()
        queue.q.extend([1, 2, 3, 4, 5, 6, 7])

        r = RateLimitingBatcher(
            queue=queue,
            wallet=Wallet(),
            sleep_interval=0,
            max_batch_size=3,
            max_txn_delay=1
        )

        r.num_batches_sent = 1
        r.txn_delay = 100

        self.assertTrue(r.ready_for_next_batch())
        self.assertEqual(r.txn_delay, 101)

    def test_remove_batch_ids_removes_id(self):
        queue = MockQueue()

        r = RateLimitingBatcher(
            queue=queue,
            wallet=Wallet(),
            sleep_interval=0,
            max_batch_size=3,
            max_txn_delay=1
        )

        r.add_batch_id('1')
        r.add_batch_id('2')
        r.add_batch_id('3')

        r.remove_batch_ids(['1', '2'])

        self.assertListEqual(r.sent_batch_ids, ['3'])

    def test_remove_batch_ids_decrements_num_batches_sent(self):
        queue = MockQueue()

        r = RateLimitingBatcher(
            queue=queue,
            wallet=Wallet(),
            sleep_interval=0,
            max_batch_size=3,
            max_txn_delay=1
        )

        r.add_batch_id('1')
        r.add_batch_id('2')
        r.add_batch_id('3')

        self.assertEqual(r.num_batches_sent, 3)

        r.remove_batch_ids(['1', '2'])

        self.assertEqual(r.num_batches_sent, 1)

    def test_remove_batch_ids_sets_sent_batch_ids_to_new_id_list_if_corruption_occurs(self):
        queue = MockQueue()

        r = RateLimitingBatcher(
            queue=queue,
            wallet=Wallet(),
            sleep_interval=0,
            max_batch_size=3,
            max_txn_delay=1
        )

        r.num_batches_sent = 1000

        r.add_batch_id('1')
        r.add_batch_id('2')
        r.add_batch_id('3')

        r.remove_batch_ids(['1', '2'])

        self.assertEqual(r.num_batches_sent, 1)

    def test_get_next_batch_size_num_tx_gte_max_batch_size_returns_smaller_size(self):
        queue = MockQueue()

        queue.q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

        r = RateLimitingBatcher(
            queue=queue,
            wallet=Wallet(),
            sleep_interval=0,
            max_batch_size=3,
            max_txn_delay=1
        )

        self.assertEqual(r.get_next_batch_size(), 3)

    def test_get_next_batch_size_num_tx_gte_max_batch_size_resets_txn_delay(self):
        queue = MockQueue()

        queue.q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

        r = RateLimitingBatcher(
            queue=queue,
            wallet=Wallet(),
            sleep_interval=0,
            max_batch_size=3,
            max_txn_delay=1000000
        )

        r.txn_delay = 10000

        r.get_next_batch_size()

        self.assertEqual(r.txn_delay, 0)

    def test_get_next_batch_size_txn_delay_gte_max_returns_smaller_size(self):
        queue = MockQueue()

        queue.q = [1]

        r = RateLimitingBatcher(
            queue=queue,
            wallet=Wallet(),
            sleep_interval=0,
            max_batch_size=3,
            max_txn_delay=1
        )
        r.txn_delay = 10000
        self.assertEqual(r.get_next_batch_size(), 1)

    def test_get_next_batch_size_txn_delay_gte_max_returns_resets_txn_delay(self):
        queue = MockQueue()

        queue.q = [1]

        r = RateLimitingBatcher(
            queue=queue,
            wallet=Wallet(),
            sleep_interval=0,
            max_batch_size=3,
            max_txn_delay=1
        )

        r.txn_delay = 10000
        r.get_next_batch_size()
        self.assertEqual(r.txn_delay, 0)

    def test_get_next_batch_num_txn_lt_max_batch_txn_delay_lt_max_returns_0(self):
        queue = MockQueue()

        queue.q = [1]

        r = RateLimitingBatcher(
            queue=queue,
            wallet=Wallet(),
            sleep_interval=0,
            max_batch_size=3,
            max_txn_delay=1
        )

        self.assertEqual(r.get_next_batch_size(), 0)

    def test_get_txn_list_filters_bad_txs(self):
        w = Wallet()
        queue = MockQueue()

        r = RateLimitingBatcher(
            queue=queue,
            wallet=w,
            sleep_interval=0,
            max_batch_size=3,
            max_txn_delay=1
        )

        a = make_good_tx(w.vk.encode())
        b = make_bad_tx()
        c = make_bad_tx()
        d = make_good_tx(w.vk.encode())

        expected = [a, d]

        queue.q.extend([(1, a), (1, b), (1, c), (1, d)])

        self.assertListEqual(r.get_txn_list(4), expected)

    def test_get_txn_list_all_if_all_good(self):
        w = Wallet()
        queue = MockQueue()

        r = RateLimitingBatcher(
            queue=queue,
            wallet=w,
            sleep_interval=0,
            max_batch_size=3,
            max_txn_delay=1
        )

        a = make_good_tx(w.vk.encode())
        b = make_good_tx(w.vk.encode())
        c = make_good_tx(w.vk.encode())
        d = make_good_tx(w.vk.encode())

        expected = [a, b, c, d]

        queue.q.extend([(1, a), (1, b), (1, c), (1, d)])

        self.assertListEqual(r.get_txn_list(4), expected)

