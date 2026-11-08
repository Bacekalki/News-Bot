from src.input_parser import parse_input
from src.command_executor import CommandExecutor

def get_response(executor : CommandExecutor, user_input : str, username : str) -> str:
    command, arguments = parse_input(user_input)
    return executor.execute_command(command, arguments, username)
