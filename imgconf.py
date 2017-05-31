#-*- coding: utf-8 -*-
import ConfigParser # cfg file parsing

import cgitb
cgitb.enable(format='text')

def extractconf():

	config = ConfigParser.ConfigParser()
	config.read('option.cfg')
	if config.has_section('extract_option'):
		options = config.items('extract_option')

	return options


def infix_to_postfix(infix_exp):
	stack = []
	postfix = []
	relational = ['>', '<', '==', '>=', '<=', '!=']
	logicalop = ['and', 'or']

	infix_exp = infix_exp.replace('(', '( ')
	infix_exp = infix_exp.replace(')', ' )')

	split_exp = infix_exp.split(' ')
	for i in split_exp:
		if(len(stack) == 0): is_empty = True
		else: is_empty = False

		if i in relational:
			stack.append(i)

		elif i in logicalop:
			peek = stack[-1:]
			if (not is_empty) and (peek in relational):
				postfix.append(stack.pop())
			stack.append(i)

		elif i == '(':
			stack.append(i)

		elif i == ')':
			top_op = stack.pop()
			while top_op != '(':
				postfix.append(top_op)
				top_op = stack.pop()

		else:
			postfix.append(i)

	while len(stack):
		postfix.append(stack.pop())

	return " ".join(postfix)

def search_condition(postfix_exp):
	exp = postfix_exp.split(" ")
	stack = []
	op = ['>', '<', '==', '>=', '<=', '!=', 'and', 'or']

	for i in exp:
		if i not in op:
			stack.append(i)
		else:
			try:
				op2 = str(stack.pop())
				op1 = str(stack.pop())
				exp = "%s %s %s" % (op1 , i ,op2)
				stack.append(eval(exp))
			except SyntaxError as e:
				print "[err] ", str(op1), str(op2), str(i), str(exp)

	return stack.pop()