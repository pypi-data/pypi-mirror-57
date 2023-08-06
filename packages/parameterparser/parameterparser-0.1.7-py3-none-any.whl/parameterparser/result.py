class Result:
    """
    Represents a Result for a Parameter.

    Attributes:
        :var value: The value for this Result.
    """
    HALT_PARSE = "parameter_parser_halt_parser"

    @staticmethod
    def halt(value=HALT_PARSE):
        """
        Retrieve a halting Result.
        :param value: The optional Value (defaults to halt only)
        :return: The Halting Result object.
        """
        return Result(value, True)

    def __init__(self, value, halt):
        """
        Create the Result object.
        :param value: The value.
        :param halt:  Whether or not this Result should halt the Parser.
        """
        self.value = value
        self.__is_halt = halt

    def should_halt(self):
        """
        Check if this Result object should Halt the Parser.
        :return: True if it should halt the parser.
        """
        return self.__is_halt
