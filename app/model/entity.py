from sqlalchemy.orm import class_mapper


class BaseModel(object):

    # 对象转出字典
    def as_dict(self):
        # return {c.name: getattr(self, c.name) for c in self.__table__.columns}
        # 上面的有缺陷，表字段和属性不一致会有问题
        return dict((col.name, getattr(self, col.name)) for col in class_mapper(self.__class__).mapped_table.c)

    # list[object] =>list[dict]
    @staticmethod
    def to_list_dict(list_model):
        list_dict = ([])
        for model in list_model:
            list_dict.append(model.as_dict())
        return list_dict
