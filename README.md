# ADPT-BE
## Overview
_ADPT-BE_ stands for _Automatic Detection of Persuation Techniques - Backend_.

The repository contains a small Flask application that loads the model and exposes an endpoint to perform model inference. 

To have a better understanding of the model and how it was created, you can check[ADPT-AI](https://github.com/TeimasTeimoso/ADPT-AI) which contains the code and research papers produced during the work.

Currently, the model created only supports inference for textual data. There are plans in the future to add image classification.

## Endpoint
| Method | Resource | Query Parameters | Body                   |
|--------| ---------| -----------------| -----                  |
| POST   | predict  | -                | {"text": $sentence, "probs": true\|false}   |

Bellow there is an example of a response setting _probs_ to _true_, and after that, an example of setting it to _false_.
``` json
{
    "Appeal to authority": 0.08427731692790985,
    "Appeal to fear/prejudice": 0.3441292643547058,
    "Bandwagon": 0.1411733627319336,
    "Black-and-white Fallacy/Dictatorship": 0.11429373919963837,
    "Causal Oversimplification": 0.14675235748291016,
    "Doubt": 0.04427878186106682,
    "Exaggeration/Minimisation": 0.5388496518135071,
    "Flag-waving": 0.3002663254737854,
    "Glittering generalities (Virtue)": 0.1867496371269226,
    "Loaded Language": 0.9543203115463257,
    "Misrepresentation of Someone's Position (Straw Man)": 0.29040059447288513,
    "Name calling/Labeling": 0.10895266383886337,
    "Obfuscation, Intentional vagueness, Confusion": 0.2316785603761673,
    "Presenting Irrelevant Data (Red Herring)": 0.03351626917719841,
    "Reductio ad hitlerum": 0.07988007366657257,
    "Repetition": 0.11493965983390808,
    "Slogans": 0.5039657950401306,
    "Smears": 0.030777540057897568,
    "Thought-terminating cliché": 0.07756602019071579,
    "Whataboutism": 0.026369892060756683
}
```
```json
[
    "Exaggeration/Minimisation",
    "Loaded Language",
    "Slogans"
]
``````
## Deployment
As the time, the service is not hosted anywhere due to free cloud providers resource limitations.

It can be deployed locally using the provided Dockerfile.