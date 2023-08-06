import datetime
from os.path import commonprefix

from typing import Optional, List


from janis_assistant.utils.dateutil import DateUtil


class WorkflowOutputModel:

    ARRAY_SEPARATOR_1 = "::"
    ARRAY_SEPARATOR_NESTED = "||"

    def __init__(
        self,
        tag,
        original_path,
        new_path,
        timestamp,
        prefix,
        tags,
        secondaries,
        extension,
    ):
        self.tag = tag
        self.originalpath = original_path
        self.newpath = new_path

        self.prefix: Optional[List[str]] = None
        if prefix:
            if isinstance(prefix, str):
                self.prefix = self.to_array(prefix)
            else:
                self.prefix = [t for t in prefix if t is not None]

        self.tags = None
        if tags:
            if isinstance(tags, str):
                self.tags = self.to_array(tags)
            else:
                self.tags = [t for t in tags if t is not None]

        self.secondaries = None
        if secondaries:
            if isinstance(secondaries, str):
                self.secondaries = self.to_array(secondaries)
            else:
                self.secondaries = secondaries

        if not isinstance(timestamp, datetime.datetime):
            timestamp = DateUtil.parse_iso(timestamp)
        self.timestamp = timestamp
        self.extension = extension

    @staticmethod
    def from_row(row):
        return WorkflowOutputModel(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
        )

    @staticmethod
    def from_array(array):
        if not array:
            return None
        """
        At most, two levels. One separated by one separator, then the second by the other
        :param array: iterable
        :return:
        """
        return WorkflowOutputModel.ARRAY_SEPARATOR_1.join(
            WorkflowOutputModel.ARRAY_SEPARATOR_NESTED.join(i)
            if isinstance(i, list)
            else str(i)
            for i in array
        )

    @staticmethod
    def to_array(value: str):
        if not value:
            return []
        s = value.split(WorkflowOutputModel.ARRAY_SEPARATOR_1)
        return [
            ss.split(WorkflowOutputModel.ARRAY_SEPARATOR_NESTED)
            if WorkflowOutputModel.ARRAY_SEPARATOR_NESTED in ss
            else ss
            for ss in s
        ]

    def format(self):
        return f"- {self.tag}: {self._format_value(self.newpath)}"

    @staticmethod
    def _format_value(value, isroot=True):
        if not value:
            return ""

        if isinstance(value, str):
            value = value.split("|")

        if isinstance(value, list):
            if len(value) == 0:
                return ""
            elif len(value) == 1:
                value = value[0]
            else:
                values = [
                    WorkflowOutputModel._format_value(v, isroot=False) for v in value
                ]
                if isroot:
                    return "(multiple) " + commonprefix(values) + "*"
                return commonprefix(values)

        if any(isinstance(value, T) for T in [str, float, int, bool]):
            return str(value)

        # hmmm, idk
        return str(value)
