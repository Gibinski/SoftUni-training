from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.documents = []
        self.topics = []


    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)


    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)


    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)


    def edit_category(self, category_id: int, new_name:str):
        category = [c for c in self.categories if c.id == category_id][0]
        category.edit(new_name)


    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [t for t in self.topics if t.id == topic_id][0]
        topic.edit(new_topic, new_storage_folder)


    def edit_document(self, document_id: int, new_file_name: str):
        document = [d for d in self.documents if d.id == document_id][0]
        document.edit(new_file_name)


    def delete_category(self, category_id):
        category = [c for c in self.categories if c.id == category_id][0]
        self.categories.remove(category)


    def delete_topic(self, topic_id):
        topic = [t for t in self.topics if t.id == topic_id][0]
        self.topics.remove(topic)


    def delete_document(self, document_id):
        document = [d for d in self.documents if d.id == document_id][0]
        self.documents.remove(document)


    def get_document(self, document_id):
        return [d for d in self.documents if d.id == document_id][0]


    def __repr__(self):
        return "\n".join([str(d) for d in self.documents])

