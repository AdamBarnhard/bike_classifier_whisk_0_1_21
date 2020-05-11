from invoke import Collection, task
import bike_classifier_whisk_0_1_21.core.tasks

# Core Tasks
ns = Collection.from_module(bike_classifier_whisk_0_1_21.core.tasks)

### Add project-specific tasks below. ###
# See http://docs.pyinvoke.org/en/stable/getting-started.html

from bike_classifier_whisk_0_1_21.models.model import Model

@task(help={'data': "A single record to perform model inference"})
def predict(c, data):
    """
    Invokes the model.
    """
    model = Model()
    print(model.predict([data]))

model = Collection('model')
model.add_task(predict)
ns.add_collection(model)
