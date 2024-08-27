"""
This is a boilerplate pipeline 'grayscaleimage'
generated using Kedro 0.19.8
"""
from kedro.pipeline import Pipeline, node, pipeline
from .nodes import resize_image, grayscale_image, add_text
def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func = resize_image,
                inputs= "original_image",
                outputs= "converted_image1",
                name= "resize_image",
            ),
            node(
                func = grayscale_image,
                inputs = "converted_image1",
                outputs = "converted_image2",
                name = "grayscale_image",
            ),
            node(
                func = add_text,
                inputs = "original_image",
                outputs="converted_image3",
                name = "add_text",
            )
        ]
    )


