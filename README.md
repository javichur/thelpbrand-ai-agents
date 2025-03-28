# The LP Brand - AI Agents

The "AI Agents" for The LP Brand project are documented here: https://javiercampos.es/blog/2025/03/27/como-cree-con-ia-una-marca-de-camisetas-tazas-carcasas-ai-agents-y-mas/

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

## Hardware and external services required

In `crew.py`, the LLM is expected to be served locally with an external application (ie: [LM Studio](https://lmstudio.ai/)). You can find more details in the blogpost linked on top. Good LLMs require an important amount of GPU memory. Consider to use the local configuration during initial steps of development, and then leverage cloud services to run this with State-of-the-Art LLMs. 

```
llm = LLM(
        model="openai/my-openai-compatible-model",
        api_key="not-required-in-lm-studio",
        base_url="http://localhost:1234/v1" # I use LM Studio application to serve LLMs during development locally.
    )
```

## Running the Project

To kickstart the crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the thelpbrand_crew Crew, assembling the agents and assigning them tasks as defined in the configuration.

Because in `crew.py` the Verbose is set True, you will see the progress with lot of details in the Terminal.

`Human input` is expected after some agent tasks (see `Tasks.yaml` or the blogpost for the specifics). If you are fine with the output, just press "intro".

The latest agent executes the task called `prompt_designer_task` and returns the prompts. Please copy those prompts and paste them one by one in [ChatGPT free version](https://chatgpt.com/) to get the desired image. Take into account that this manual step can be automated via GhatGPT API but it wouldn't be [https://openai.com/api/pricing/](free).


## Understanding Your Crew

The thelpbrand_crew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.
