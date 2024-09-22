import factory

from contexts.shared.domain.image import Image


class ImageFactory(factory.Factory):
    class Meta:
        model = Image

    path = factory.Faker("file_path", extension="jpg")
