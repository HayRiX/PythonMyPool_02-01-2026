from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return result string"""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor"""
        pass

    def format_output(self, result: str) -> str:
        """Format the output string (Default implementation)"""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for n in data:
                if not isinstance(n, (int, float)):
                    return False
            return True
        return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data type for NumericProcessor")
        data_len = len(data)
        data_sum = sum(data)
        data_average = data_sum / data_len
        return (f"Processed {data_len} numeric values, sum={data_sum}, "
                f"avg={data_average}")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise TypeError("Invalid data type for TextProcessor")
        data_len = len(data)
        words_n = len(data.split(' '))
        return f"Processed text: {data_len} characters, {words_n} words"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str) and ':' in data:
            return True
        return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise TypeError("Invalid data type for LogProcessor")
        levle, msg = data.split(':', 1)
        if (levle == "ERROR"):
            return f"[ALERT] {levle} level detected: {msg.strip()}"
        else:
            return f"[INFO] {levle} level detected: {msg.strip()}"


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    data = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    num_processor = NumericProcessor()
    if num_processor.validate(data):
        print("Validation: Numeric data verified")
        result = num_processor.process(data)
        final_output = num_processor.format_output(result)
        print(final_output)

    print("\nInitializing Text Processor...")
    data = "Hello Nexus World"
    print(f'Processing data: "{data}"')
    txt_processor = TextProcessor()
    if txt_processor.validate(data):
        print("Validation: Text data verified")
        result = txt_processor.process(data)
        final_output = txt_processor.format_output(result)
        print(final_output)

    print("\nInitializing Log Processor...")
    data = "ERROR: Connection timeout"
    print(f'Processing data: "{data}"')
    log_processor = LogProcessor()
    if log_processor.validate(data):
        print("Validation: Log entry verified")
        result = log_processor.process(data)
        final_output = log_processor.format_output(result)
        print(final_output)

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    data1 = [1, 2, 3]
    data2 = "Hello World!"
    data3 = "INFO: System ready"

    try:
        result = num_processor.process(data1)
        print(f"Result 1: {result}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        result = txt_processor.process(data2)
        print(f"Result 2: {result}")
    except TypeError as e:
        print(f"Error: {e}")

    try:
        result = log_processor.process(data3)
        print(f"Result 3: {result}")
    except TypeError as e:
        print(f"Error: {e}")

    finally:
        print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
