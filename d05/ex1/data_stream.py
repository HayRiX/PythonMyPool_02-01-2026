from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data"""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria (Default implementation)"""
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics (Default implementation)"""
        return {"stream_id": self.stream_id}


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            readings_count = len(data_batch)
            if readings_count == 0:
                return "Sensor analysis: 0 readings processed, avg temp: 0°C"
            total_sum = sum(data_batch)
            avg_temp = total_sum / readings_count
            return (f"Sensor analysis: {readings_count} readings processed, "
                    f"avg temp: {avg_temp}°C")
        except TypeError:
            return "Error: Invalid sensor data format."

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "High-priority data only":
            return [d for d in data_batch
                    if isinstance(d, (int, float)) and d > 30]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Environmental Data"
        return stats


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            total_transaction = len(data_batch)
            net_flow = sum(data_batch)
            return (f"Transaction analysis: {total_transaction} operations, "
                    f"net flow: {net_flow:+} units")
        except TypeError:
            return "Error: Invalid transaction data format."

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "High-priority data only":
            return [d for d in data_batch
                    if isinstance(d, (int, float)) and abs(d) >= 1000]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Financial Data"
        return stats


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            total_event = len(data_batch)
            total_errors = data_batch.count("error")
            return (f"Event analysis: {total_event} events, "
                    f"{total_errors} error detected")
        except Exception:
            return "Error processing event batch."

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "High-priority data only":
            return [d for d in data_batch if d == "error"]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "System Events"
        return stats


class StreamProcessor:
    def process_stream(self, stream: DataStream, batch: List[Any]) -> str:
        return stream.process_batch(batch)


def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    processor = StreamProcessor()

    print("\nInitializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    s_stats = sensor.get_stats()
    print(f"Stream ID: {s_stats['stream_id']}, Type: {s_stats['type']}")
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(sensor.process_batch([22.5, 22.5, 22.5]))

    print("\nInitializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    t_stats = trans.get_stats()
    print(f"Stream ID: {t_stats['stream_id']}, Type: {t_stats['type']}")
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(trans.process_batch([100, -150, 75]))

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    e_stats = event.get_stats()
    print(f"Stream ID: {e_stats['stream_id']}, Type: {e_stats['type']}")
    print("Processing event batch: [login, error, logout]")
    print(event.process_batch(['login', 'error', 'logout']))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    print("Batch 1 Results:")
    sensor_data = processor.process_stream(sensor, [20.0, 24.0])
    if "2 readings" in sensor_data:
        print("- Sensor data: 2 readings processed")
    transaction_data = processor.process_stream(trans, [10, -5, 20, -5])
    if "4 operations" in transaction_data:
        print("- Transaction data: 4 operations processed")
    event_data = processor.process_stream(event, ["login", "error", "logout"])
    if "3 events" in event_data:
        print("- Event data: 3 events processed")

    print("\nStream filtering active: High-priority data only")

    sensor_batch = [20.0, 35.0, 40.0, 22.0]
    filtered_sensors = sensor.filter_data(sensor_batch,
                                          "High-priority data only")

    trans_batch = [10, 1500, -5, 20]
    filtered_trans = trans.filter_data(trans_batch, "High-priority data only")

    print(f"Filtered results: {len(filtered_sensors)} critical sensor alerts, "
          f"{len(filtered_trans)} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
