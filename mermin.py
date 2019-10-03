import argparse
import numpy as np
import random


class Mermin(object):
	def __init__(self, ro):
		self.switch_number = 3
		self.lamp_number = 3
		self.round = ro

		self.seq1 = [0, 0, 1]
		self.seq2 = [0, 0, 1]

		self.rr = 0
		self.rg = 0
		self.rn = 0
		self.gr = 0
		self.gg = 0
		self.gn = 0

		self.same = 0
		self.diff = 0
		self.null = 0

		self.n = None

	def case1(self):
		self.seq1 = [0, 0, 0]  # R: 0, G: 1
		self.seq2 = [0, 0, 0]

		for r in range(self.round):
			sw = random.sample(range(self.switch_number), 2)
			sw1 = sw[0]  # A machine switches
			sw2 = sw[1]  # B machine switches

			if self.seq1[sw1] == self.seq2[sw2]: 
				self.same += 1

		prob = float(self.same) / self.round
		print prob

		return prob

	def case2(self):
		self.seq1 = [0, 0, 1]  # R: 0, G: 1
		self.seq2 = [0, 0, 1]

		for r in range(self.round):
			sw = random.sample(range(self.switch_number), 2)
			sw1 = sw[0]  # A machine switches
			sw2 = sw[1]  # B machine switches

			if self.seq1[sw1] == self.seq2[sw2]: 
				self.same += 1
			else: 
				self.diff += 1

		prob = float(self.same) / self.round
		print prob

		return prob

	def case3(self):
		self.seq1 = [0, 0, 0]  # R: 0, G: 1
		self.seq2 = [0, 0, 2]  # N: 2

		for r in range(self.round):
			sw = random.sample(range(self.switch_number), 2)
			sw1 = sw[0]  # A machine switches
			sw2 = sw[1]  # B machine switches

			if self.seq2[sw2] == 2:
				self.null += 1
				continue
			elif self.seq1[sw1] == self.seq2[sw2]: 
				self.same += 1
			else: 
				self.diff += 1

		prob = float(self.same) / (self.round-self.null)
		print prob

		return prob

	def case4(self):
		self.seq1 = [0, 0, 1]  # R: 0, G: 1
		self.seq2 = [0, 2, 1]  # N: 2

		for r in range(self.round):
			sw = random.sample(range(self.switch_number), 2)
			sw1 = sw[0]  # A machine switches
			sw2 = sw[1]  # B machine switches

			if self.seq2[sw2] == 2:
				self.null += 1
				continue
			elif self.seq1[sw1] == self.seq2[sw2]: 
				self.same += 1
			else: 
				self.diff += 1

		prob = float(self.same) / (self.round-self.null)
		print prob

		return prob	

	def case5(self):
		self.seq1 = [0, 0, 1]  #R:0, G:1
		self.seq2 = [0, 0, 2]  #N:2

		for r in range(self.round):
			sw = random.sample(range(self.switch_number), 2)
			sw1 = sw[0]  # A machine switches
			sw2 = sw[1]  # B machine switches

			if self.seq2[sw2] == 2:
				self.null += 1
				continue
			elif self.seq1[sw1] == self.seq2[sw2]: 
				self.same += 1
			else: 
				self.diff += 1

		prob = float(self.same)/(self.round-self.null)
		print prob

		return prob	


def main(args=None):
	parser = argparse.ArgumentParser(description='Define the rounds.')

	parser.add_argument('--round', metavar='R', type=int, nargs='?',
                    help='an integer for round', default=10000000)

	args = parser.parse_args()

	print "Start the Mermin Experiment..."
	print "Your experiment will run for %d rounds" % (args.round)
	
	mermin = Mermin(args.round)
	mermin.case1()

	
if __name__ == '__main__':
	main()


