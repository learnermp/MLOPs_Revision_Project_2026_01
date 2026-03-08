from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str


@dataclass
class DataValidationArtifact:
    validation_status:bool  # If it is true then next step of transformation will run.
    message: str
    drift_report_file_path: str