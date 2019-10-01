from __future__ import print_function

C_RESET = ''
C_GREEN = ''
C_RED = ''
C_CYAN = ''
C_YELLOW = ''

_prints_enabled = False

def enable_prints():
	global \
		C_RESET, C_GREEN, C_RED, \
			C_CYAN, C_YELLOW

	from colorama import init, Fore

	init(convert=True)
	C_RESET = Fore.RESET
	C_GREEN = Fore.GREEN
	C_RED = Fore.RED
	C_CYAN = Fore.CYAN
	C_YELLOW = Fore.YELLOW

	_prints_enabled = True


table = """
 Id:    Type:           Payload:        Admin:          Description:
 ----   -----------     -----------     --------        -----------------------"""


class Constant(object):
	__slots__ = ('output',)

	output = []


def reset_output():
	Constant.output = []


def print_table():
	if _prints_enabled:
		print(table)

	Constant.output.append(("t", table))


def table_success(id, message):
	if _prints_enabled:
		print(C_GREEN + " " + id + C_RESET + message)

	Constant.output.append(("ok", id + message))


def table_error(id, message):
	if _prints_enabled:
		print(C_RED + " " + id + C_RESET + message)

	Constant.output.append(("error", id + message))


def print_success(message):
	if _prints_enabled:
		print(C_GREEN + " [+] " + C_RESET + message)

	Constant.output.append(("ok", message))


def print_error(message):
	if _prints_enabled:
		print(C_RED + " [-] " + C_RESET + message)

	Constant.output.append(("error", message))


def print_info(message):
	if _prints_enabled:
		print(C_CYAN + " [!] " + C_RESET + message)

	Constant.output.append(("info", message))


def print_warning(message):
	if _prints_enabled:
		print(C_YELLOW + " [!] " + C_RESET + message)

	Constant.output.append(("warning", message))
