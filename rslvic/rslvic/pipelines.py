import json


class JsonWriterPipeline(object):
    def open_spider(self, spider):
        self.file = open('rslvic.json', 'w')
        self.file.write('[')
        self.line_buffer = []

    def close_spider(self, spider):
        if len(self.line_buffer) > 0:
            self.file.write(self.line_buffer.pop() + "\n")
        self.file.write("]")

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False)
        if len(self.line_buffer) > 0:
            self.file.write(self.line_buffer.pop() + ",\n")
        self.line_buffer.append(line)
        return item
