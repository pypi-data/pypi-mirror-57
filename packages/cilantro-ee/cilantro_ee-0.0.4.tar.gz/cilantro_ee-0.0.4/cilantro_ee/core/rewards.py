from contracting.client import ContractingClient
from contracting.db.driver import ContractDriver
from cilantro_ee.services.storage.vkbook import PhoneBook
import capnp
import os
from cilantro_ee.messages import capnp as schemas

blockdata_capnp = capnp.load(os.path.dirname(schemas.__file__) + '/blockdata.capnp')

PENDING_REWARDS_KEY = '__rewards'


class RewardManager:
    def __init__(self, driver=ContractDriver(), client=ContractingClient()):
        self.driver = driver
        self.client = client

        self.stamp_contract = self.client.get_contract('stamp_cost')
        self.reward_contract = self.client.get_contract('rewards')
        self.currency_contract = self.client.get_contract('currency')

        assert self.stamp_contract is not None, 'Stamp contract not in state.'
        assert self.reward_contract is not None, 'Reward contract not in state.'
        assert self.currency_contract is not None, 'Currency contract not in state.'

    def issue_rewards(self):
        master_ratio, delegate_ratio, burn_ratio, foundation_ratio = self.reward_ratio
        pending_rewards = self.get_pending_rewards()

        masters = PhoneBook.masternodes
        delegates = PhoneBook.delegates

        master_reward = (master_ratio * pending_rewards) / len(masters)
        delegate_reward = (delegate_ratio * pending_rewards) / len(delegates)
        foundation_reward = foundation_ratio * pending_rewards

        for m in masters:
            self.add_to_balance(vk=m, amount=master_reward)

        for d in delegates:
            self.add_to_balance(vk=d, amount=delegate_reward)

        self.set_pending_rewards(0)

    def add_to_balance(self, vk, amount):
        current_balance = self.currency_contract.quick_read(variable='balances', key=vk) or 0
        self.currency_contract.quick_write(variable='balances', key=vk, value=amount + current_balance)

    def get_pending_rewards(self):
        return self.driver.get(PENDING_REWARDS_KEY) or 0

    def set_pending_rewards(self, value):
        self.driver.set(PENDING_REWARDS_KEY, value=value)

    @property
    def stamps_per_tau(self):
        return self.stamp_contract.quick_read('S', 'rate')

    @staticmethod
    def stamps_in_block(block):
        total = 0

        for sb in block.subBlocks:
            for tx in sb.transactions:
                total += tx.stampsUsed

        return total

    @staticmethod
    def stamps_in_subblock(subblock):
        total = 0

        for tx in subblock.transactions:
            total += tx.stampsUsed

        return total

    def add_pending_rewards(self, subblock):
        current_rewards = self.get_pending_rewards()
        used_stamps = self.stamps_in_subblock(subblock)

        rewards_as_tau = used_stamps / self.stamps_per_tau
        self.set_pending_rewards(current_rewards + rewards_as_tau)

    @property
    def reward_ratio(self):
        return self.reward_contract.quick_read(variable='value')
