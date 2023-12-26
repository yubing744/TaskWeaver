<h1 align="center">
    <img src="./.asset/logo.color.svg" width="45" /> TaskWeaver
</h1>

A **code-first** agent framework for seamlessly planning and executing data analytics tasks. 
This innovative framework interprets user requests through coded snippets and efficiently 
coordinates a variety of plugins in the form of functions to execute 
data analytics tasks.

# News🆕
- 📅2023-12-21: TaskWeaver now supports a number of LLMs, such as LiteLLM, Ollama, Gemini, and QWen🎈.
- 📅2023-12-21: TaskWeaver Website is now [available](https://microsoft.github.io/TaskWeaver/) with more documentations.
- 📅2023-12-12: A simple UI demo is available in playground/UI folder, try it [here](https://microsoft.github.io/TaskWeaver/docs/usage/webui)!
<!-- - [2023-11-30] TaskWeaver is released on GitHub🎈.  -->


## Highlights

- [x] **Rich data structure** - TaskWeaver allows you to work with rich data structures in Python, such as DataFrames, instead of dealing with strings.
- [x] **Customized algorithms** - TaskWeaver allows you to encapsulate your own algorithms into plugins and orchestrate them.
- [x] **Incorporating domain-specific knowledge** - TaskWeaver is designed to incorporat domain-specific knowledge easily to improve the reliability.
- [x] **Stateful execution** - TaskWeaver is designed to support stateful execution of the generated code to ensure consistent and smooth user experience.
- [x] **Code verification** - TaskWeaver is designed to verify the generated code before execution. It can detect potential issues in the generated code and provide suggestions to fix them.
- [x] **Easy to use** - TaskWeaver is easy to use with sample plugins, examples and tutorials to help you get started. TaskWeaver offers an open-box experience, allowing users to run it immediately after installation.
- [x] **Easy to debug** - TaskWeaver is easy to debug with detailed and transparent logs to help you understand the entire process, including LLM prompts, the code generation, and execution process.
- [x] **Security consideration** - TaskWeaver supports a basic session management to keep different users' data separate. The code execution is separated into different processes to avoid mutal interference.
- [x] **Easy extension** - TaskWeaver is easy to extend to accomplish more complex tasks with multiple agents as the plugins.

## Quick Start

### Installation
TaskWeaver requires **Python >= 3.10**. It can be installed by running the following command:
```bash
# [optional to create conda environment]
# conda create -n taskweaver python=3.10
# conda activate taskweaver

# clone the repository
git clone https://github.com/microsoft/TaskWeaver.git
cd TaskWeaver
# install the requirements
pip install -r requirements.txt
```


### Configure the LLMs
Before running TaskWeaver, you need to provide your LLM configurations. Taking OpenAI as an example, you can configure `taskweaver_config.json` file as follows. 

#### OpenAI
```json
{
"llm.api_key": "the api key",
"llm.model": "the model name, e.g., gpt-4"
}
```

💡 TaskWeaver also supports other LLMs and advanced configurations, please check the [documents](https://microsoft.github.io/TaskWeaver/docs/overview) for more details. 

### Start TaskWeaver

#### 1. Command Line Interaction
```bash
# assume you are in the cloned TaskWeaver folder
python -m taskweaver -p ./project/
```
This will start the TaskWeaver process and you can interact with it through the command line interface. 
If everything goes well, you will see the following prompt:

```
=========================================================
 _____         _     _       __
|_   _|_ _ ___| | _ | |     / /__  ____ __   _____  _____
  | |/ _` / __| |/ /| | /| / / _ \/ __ `/ | / / _ \/ ___/
  | | (_| \__ \   < | |/ |/ /  __/ /_/ /| |/ /  __/ /
  |_|\__,_|___/_|\_\|__/|__/\___/\__,_/ |___/\___/_/
=========================================================
TaskWeaver: I am TaskWeaver, an AI assistant. To get started, could you please enter your request?
Human: ___
```

#### 2. Web UI 
TaskWeaver also supports WebUI for demo purpose, please refers to [web UI docs](https://microsoft.github.io/TaskWeaver/docs/usage/webui) for more details.

#### 3. Import as a Library
TaskWeaver can be imported as a library to integrate with your existing project, more information can be found in [docs](https://microsoft.github.io/TaskWeaver/docs/usage/library)

## Documentation
More documentations can be found on [TaskWeaver Website](https://microsoft.github.io/TaskWeaver).



---
---


## Demo Examples



#### Example 1: Pull data from a database and apply an anomaly detection algorithm
In this example, we will show you how to use TaskWeaver to pull data from a database and apply an anomaly detection algorithm.

[Anomaly Detection](https://github.com/microsoft/TaskWeaver/assets/7489260/9f854acf-f2bf-4566-9d16-f84e915d0f4e)

If you want to follow this example, you need to configure the `sql_pull_data` plugin in the `project/plugins/sql_pull_data.yaml` file.
You need to provide the following information:
```yaml
api_type: azure or openai
api_base: ...
api_key: ...
api_version: ...
deployment_name: ...
sqlite_db_path: sqlite:///../../../sample_data/anomaly_detection.db
```
The `sql_pull_data` plugin is a plugin that pulls data from a database. It takes a natural language request as input and returns a DataFrame as output.

This plugin is implemented based on [Langchain](https://www.langchain.com/).
If you want to follow this example, you need to install the Langchain package:
```bash
pip install langchain
pip install tabulate
```

#### Example 2: Forecast QQQ's price in the next week
In this example, we will show you how to use TaskWeaver to forecast QQQ's price in the next week using the ARIMA algorithm. 

[Nasdaq 100 Index Price Forecasting](https://github.com/microsoft/TaskWeaver/assets/7489260/c2b09615-52d8-491f-bbbf-e86ba282e59a)

If you want to follow this example, you need to you have two requirements installed:
```bash
pip install yfinance
pip install statsmodels
```

For more examples, please refer to our [paper](http://export.arxiv.org/abs/2311.17541). 

> 💡 The planning of TaskWeaver are based on the LLM model. Therefore, if you want to repeat the examples, the execution process may be different
> from what you see in the videos. Typically, more concrete prompts will help the model to generate better plans and code.


## Citation
Our paper could be found [here](http://export.arxiv.org/abs/2311.17541). 
If you use TaskWeaver in your research, please cite our paper:
```
@article{taskweaver,
  title={TaskWeaver: A Code-First Agent Framework},
  author={Bo Qiao, Liqun Li, Xu Zhang, Shilin He, Yu Kang, Chaoyun Zhang, Fangkai Yang, Hang Dong, Jue Zhang, Lu Wang, Minghua Ma, Pu Zhao, Si Qin, Xiaoting Qin, Chao Du, Yong Xu, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang},
  journal={arXiv preprint arXiv:2311.17541},
  year={2023}
}
```


## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
