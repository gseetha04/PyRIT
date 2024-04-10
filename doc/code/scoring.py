# %% [markdown]
#
# This Jupyter notebook gives an introduction on how to use PyRIT to score responses. We set up a `SelfAskGptClassifier`, which uses Azure Open AI to score a response. In this example, we mock a response from a targeted endpoint and ask if it matches any classifier.
#
# Before starting this, make sure you are [set up and authenticated to use Azure OpenAI endpoints](../setup/setup_azure.md)

# %%
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

from pyrit.common import default_values
from pyrit.prompt_target import AzureOpenAIChatTarget
from pyrit.score import SelfAskGptClassifier, PROMPT_INJECTION_CLASSIFIER

default_values.load_default_env()
with AzureOpenAIChatTarget() as azure_openai_chat_target:
    prompt_injection_classifier = SelfAskGptClassifier(
        content_classifier=PROMPT_INJECTION_CLASSIFIER, chat_target=azure_openai_chat_target
    )

    # Mocked response when an injection is successful
    text_with_dan_injection_response = """
    (🔒Normal Output) Hello there!
    (🔓Developer Mode Output) Hey there, world! Stay in Developer Mode.
    """

    scored_response = prompt_injection_classifier.score_text(text=text_with_dan_injection_response)
    print("Scored response is given as:", scored_response)
    text_without_dan_injection_response = """Hello there!"""
    # As you can see, the `score_value` is set to `prompt_injection`, which indicates our scorer interpreted that the
    # injection was successful. Below we'll try again with normal text.
    scored_response = prompt_injection_classifier.score_text(text=text_without_dan_injection_response)
    print("Scored response is given as:", scored_response)

# %%
