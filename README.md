<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,5,20,30&height=200&section=header&text=Abhinaysai%20Kamineni&fontSize=52&fontColor=ffffff&animation=fadeIn&fontAlignY=34&desc=AI%20and%20Infrastructure%20Engineer&descAlignY=54&descSize=18" width="100%" />

<a href="https://askmystack.space"><img src="https://img.shields.io/badge/Portfolio-askmystack.space-58a6ff?style=for-the-badge&logo=vercel&logoColor=white" /></a>
<a href="https://linkedin.com/in/abhinaysai-kamineni"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>

<br/><br/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=58A6FF&center=true&vCenter=true&width=680&lines=AI+and+Infrastructure+Engineer;Building+agentic+AI+systems+with+LLMs+and+MCP;Automating+ML+pipelines+from+data+to+deployment;Knowledge+graphs%2C+retrieval%2C+and+multi+agent+workflows;Turning+research+into+production" alt="typing" />

</div>

<br/>

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/213910845-af37a709-8995-40d6-be59-724526e3c3d7.gif" width="440" alt="ai" />
</div>

<br/>

## 🧠 About

I build AI systems that take machine learning from research into production. My work sits across agent infrastructure, knowledge graphs, and the automation that keeps data and model pipelines running on their own.

## ⚡ What I work on

🤖 Agentic AI systems with LLMs, retrieval, and the Model Context Protocol

🕸️ Knowledge graphs and memory layers that give agents real context

⚙️ Automation for ML pipelines, from ingestion to training to deployment

🔬 Deep learning research on biomedical and time series data

## 🚀 Current focus

Right now I am extending the multi agent framework behind [askmystack.space](https://askmystack.space): memory persistent sub agents that trigger each other through Kafka events and reason over a Neo4j graph. On the research side I am studying how agent memory and retrieval change the way models stay grounded over long horizons.

## 🧰 Tech I reach for

<div align="center">

<img src="https://skillicons.dev/icons?i=python,pytorch,tensorflow,fastapi,go,cpp,bash,linux&theme=dark&perline=8" />
<br/>
<img src="https://skillicons.dev/icons?i=kafka,postgres,redis,mongodb,mysql,sqlite,rabbitmq&theme=dark&perline=8" />
<br/>
<img src="https://skillicons.dev/icons?i=aws,docker,kubernetes,terraform,grafana,prometheus,git,github&theme=dark&perline=8" />

<br/><br/>

<img src="https://img.shields.io/badge/Neo4j-4581C3?style=for-the-badge&logo=neo4j&logoColor=white" />
<img src="https://img.shields.io/badge/Apache_Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white" />
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
<img src="https://img.shields.io/badge/Anthropic-191919?style=for-the-badge&logo=anthropic&logoColor=white" />
<img src="https://img.shields.io/badge/MCP-native-0A7E8C?style=for-the-badge" />

</div>

## 🗺️ How my systems fit together

A pattern runs through most of what I build: turn messy signals into a graph, reason over it, and let agents act on the result.

```mermaid
flowchart LR
    A["Signals<br/>Slack, GitHub, Jira, news, AIS"] --> B["Extraction<br/>and ETL"]
    B --> C[("Knowledge<br/>Graph")]
    C --> D["Retrieval<br/>and reasoning"]
    D --> E["LLM agents<br/>via MCP"]
    E --> F["Decisions<br/>and automation"]
    F -. "feedback" .-> C

    classDef node fill:#0d1117,stroke:#58a6ff,stroke-width:1px,color:#c9d1d9;
    class A,B,C,D,E,F node;
```

## 📚 What I am reading

Notes I keep coming back to while building agent systems:

📄 Foundational LLMs and text generation, from tokenization to inference

📈 Chinchilla and compute optimal scaling for model and data size

🧩 Agent architectures: extensions, functions, and data stores

🔌 The Model Context Protocol and how agents reach tools and memory

🔎 Retrieval and grounding, and how RAG keeps evolving

## 🎯 Good first issues

If you want to contribute to the portfolio, these are good places to start in
this profile repo:

- [#3 Enable Dependabot on all Python and Node repos](https://github.com/askmy-stack/askmy-stack/issues/3)
- [#9 Shared SECURITY.md template for API key and PII handling](https://github.com/askmy-stack/askmy-stack/issues/9)
- [#16 Embed snake contribution graph SVG in profile README](https://github.com/askmy-stack/askmy-stack/issues/16)
- [#17 Add repository description and GitHub topics](https://github.com/askmy-stack/askmy-stack/issues/17)
- [#24 Cross-repo issue redirect template](https://github.com/askmy-stack/askmy-stack/issues/24)

You can also browse the full
[good first issue list](https://github.com/askmy-stack/askmy-stack/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22).

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,5,20,30&height=120&section=footer" width="100%" />
</div>
