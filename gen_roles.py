CSS = open("index.html").read().split("<style>")[1].split("</style>")[0]

def page(fn, title, a1,a2,a3, roles, lead, stats, about_h, about_p, projects, skills, exp, certs, contact_h):
    role_js = ",".join('"%s"'%r for r in roles)
    stat_html = "".join(
      f'<div class="stat"><div class="num grad" data-to="{t}" data-suffix="{s}">0</div><div class="lbl">{l}</div></div>'
      for t,s,l in stats)
    proj_html=""
    for tag,name,desc,stack,link,ltext in projects:
        chips="".join(f"<span>{x}</span>" for x in stack)
        proj_html+=f'<div class="pcard"><div class="ptag">{tag}</div><h3>{name}</h3><p>{desc}</p><div class="stackrow">{chips}</div><a class="plink" href="{link}" target="_blank">{ltext} &#8599;</a></div>'
    skill_html=""
    for h,tags in skills:
        t="".join(f"<span>{x}</span>" for x in tags)
        skill_html+=f'<div class="skillcard"><h4><i>&#9670;</i>{h}</h4><div class="tags">{t}</div></div>'
    exp_html=""
    for h,d,bl in exp:
        lis="".join(f"<li>{b}</li>" for b in bl)
        exp_html+=f'<div class="item"><div class="top"><h3>{h}</h3><span class="date">{d}</span></div><ul>{lis}</ul></div>'
    cert_html="".join(f'<div class="cert"><div class="ic">&#9729;</div>{c}</div>' for c in certs)
    html=f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>{CSS}
:root{{--a1:{a1};--a2:{a2};--a3:{a3}}}
</style></head><body>
<div class="aurora"><span></span><span></span><span></span></div>
<nav><div class="wrap"><div class="brand">SRB<span class="dot">.</span></div>
<div class="navlinks"><a href="./index.html">Home</a><a href="#projects">Projects</a><a href="#skills">Skills</a><a href="#experience">Experience</a><a href="mailto:srivignabandela0507@gmail.com" class="btn btn-primary">Contact</a></div></div></nav>
<header><div class="wrap">
<div class="pill"><span class="live"></span> {lead[0]}</div>
<h1>Srivigna Reddy <span class="grad">Bandela</span></h1>
<div class="rolewrap"><span id="role" class="grad"></span></div>
<p class="lead">{lead[1]}</p>
<div class="cta"><a href="#projects" class="btn btn-primary">View my work</a>
<a href="https://github.com/Bandelasrivigna" target="_blank" class="btn btn-ghost">GitHub &#8599;</a>
<a href="https://www.linkedin.com/in/srivigna-reddy-bandela-379b51229/" target="_blank" class="btn btn-ghost">LinkedIn &#8599;</a></div>
<div class="stats reveal">{stat_html}</div></div></header>
<section class="about reveal"><div class="wrap"><div class="eyebrow">About</div><h2>{about_h}</h2><p>{about_p}</p></div></section>
<section id="projects" class="reveal"><div class="wrap"><div class="eyebrow">Selected Work</div><h2>Projects</h2><div class="projects">{proj_html}</div></div></section>
<section id="skills" class="reveal"><div class="wrap"><div class="eyebrow">Toolbox</div><h2>Skills</h2><div class="skillgrid">{skill_html}</div></div></section>
<section id="experience" class="reveal"><div class="wrap"><div class="eyebrow">Journey</div><h2>Experience</h2><div class="tl">{exp_html}</div></div></section>
<section class="reveal"><div class="wrap"><div class="eyebrow">Credentials</div><h2>Certifications</h2><div class="certs">{cert_html}</div></div></section>
<section class="contact reveal"><div class="wrap"><div class="eyebrow">Let's talk</div><h2>{contact_h}</h2>
<p>Open to new roles and always happy to talk shop. Let's connect.</p>
<div class="cta" style="justify-content:center"><a href="mailto:srivignabandela0507@gmail.com" class="btn btn-primary">Email me</a>
<a href="https://www.linkedin.com/in/srivigna-reddy-bandela-379b51229/" target="_blank" class="btn btn-ghost">LinkedIn &#8599;</a>
<a href="https://github.com/Bandelasrivigna" target="_blank" class="btn btn-ghost">GitHub &#8599;</a></div></div></section>
<footer><div class="wrap">© 2026 Srivigna Reddy Bandela · <a href="./index.html" style="color:var(--a1)">Back to home</a></div></footer>
<script>
const roles=[{role_js}];let ri=0,ci=0,del=false;const el=document.getElementById('role');
(function type(){{const w=roles[ri];el.textContent=w.slice(0,ci);
if(!del&&ci<w.length){{ci++;setTimeout(type,90);}}else if(!del&&ci===w.length){{del=true;setTimeout(type,1400);}}
else if(del&&ci>0){{ci--;setTimeout(type,45);}}else{{del=false;ri=(ri+1)%roles.length;setTimeout(type,300);}}}})();
const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting)e.target.classList.add('on')}}),{{threshold:.12}});
document.querySelectorAll('.reveal').forEach(x=>io.observe(x));
function countUp(n){{const to=+n.dataset.to,s=n.dataset.suffix||"";let v=0,st=to/40;const t=setInterval(()=>{{v+=st;if(v>=to){{v=to;clearInterval(t);}}n.textContent=Math.round(v)+s;}},22);}}
const so=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.querySelectorAll('.num').forEach(countUp);so.unobserve(e.target);}}}}),{{threshold:.4}});
document.querySelectorAll('.stats').forEach(x=>so.observe(x));
</script></body></html>'''
    open(fn,"w").write(html)
    print("wrote",fn)

# ---------- DATA ENGINEER ----------
page("data-engineer.html","Srivigna Reddy Bandela — Data Engineer",
 "#5b8cff","#7b6bff","#31d6c7",
 ["Data Engineer","Pipeline Builder","Platform Engineer","ETL Specialist"],
 ["Open to Data Engineer roles","I design ETL/ELT pipelines and cloud data platforms that move terabytes a day and keep every number trustworthy."],
 [("3","+","Years experience"),("40","%","Faster refresh"),("15","+","Source systems"),("4","","Certifications")],
 "Building the pipelines that power the business",
 "Data Engineer with 3 years building production ETL/ELT pipelines, dimensional data models, and cloud data platforms on AWS, Snowflake, dbt, and Airflow. I obsess over data quality, pipeline performance, and clean design — and I bring ML and GenAI into data workflows where it earns its place. Completing an MS in Computer Science (GPA 3.90).",
 [("AI · LLM · RAG","IntelliQuery","Natural-language-to-SQL assistant: ask in English, it retrieves the schema, generates safe read-only SQL with an LLM, validates against guardrails, and returns the answer. FastAPI + RAG semantic layer.",["Python","FastAPI","LLM","RAG","SQL"],"https://github.com/Bandelasrivigna/IntelliQuery","View code"),
  ("Data Engineering","PipeFlow","End-to-end ETL/ELT pipeline ingesting millions of records per run from multiple sources into a clean, well-modeled warehouse — Spark, dbt, and Airflow with data-quality validation on every load.",["Spark","dbt","Airflow","SQL","Data Quality"],"https://github.com/Bandelasrivigna","GitHub"),
  ("ML · Analytics","RiskIntel","Classification & scoring platform over large record volumes using gradient-boosted models and real-time dashboards, cutting manual review effort by 70%.",["XGBoost","Python","Dashboards","ML"],"https://github.com/Bandelasrivigna","GitHub")],
 [("Data Engineering",["Python","SQL","PySpark","Apache Spark","Kafka","Airflow","dbt","ETL/ELT","Data Modeling","Data Warehousing"]),
  ("Cloud & DevOps",["AWS","GCP / BigQuery","Snowflake","Databricks","Docker","CI/CD","Git"]),
  ("Machine Learning & AI",["scikit-learn","XGBoost","TensorFlow","LLMs","RAG","Prompt Engineering"]),
  ("Databases",["PostgreSQL","Snowflake","Redshift","BigQuery","DynamoDB","MongoDB"])],
 [("Data Engineer — HCL Technologies","Aug 2022 – Jul 2024",
   ["Built ETL/ELT pipelines processing several TB daily from 15+ sources; cut report-refresh times 40%.",
    "Designed dimensional models & continuous data-quality checks that reduced pipeline incidents.",
    "Engineered ML models & integrated LLM/RAG into internal tools, reaching 90%+ accuracy."]),
  ("Associate Software Engineer — ApheX (Startup)","Jul 2021 – Apr 2022",
   ["Architected the startup's first data pipelines & model-serving APIs from scratch.",
    "Owned data reliability end to end with source control and testing."]),
  ("M.S. Computer Science — Governors State University","Aug 2024 – May 2026",
   ["GPA 3.90 · Data Engineering, Machine Learning, Distributed Systems."])],
 ["Google Professional Data Engineer","AWS Certified Data Engineer","AWS Certified Machine Learning","dbt Analytics Engineer"],
 "Need pipelines you can trust?")

# ---------- DATA ANALYST ----------
page("data-analyst.html","Srivigna Reddy Bandela — Analytics Engineer",
 "#31d6c7","#3fb98a","#5b8cff",
 ["Data Analyst","Analytics Engineer","BI Developer","Insights Partner"],
 ["Open to Analytics & Data Analyst roles","I turn messy, conflicting data into one source of truth — governed metrics, clean dashboards, and answers people actually trust."],
 [("3","+","Years experience"),("25","+","Data-quality checks"),("60","%","Fewer corrections"),("3","","Certifications")],
 "Turning data into decisions people trust",
 "Analytics Engineer and Data Analyst with 3 years turning complex data into clear, trusted insights. Strong in advanced SQL, dbt, and BI (Tableau, Power BI), building dimensional and semantic models, governed metrics layers, and data-quality frameworks. I bridge the gap between raw data and confident business decisions. Completing an MS in Computer Science (GPA 3.90).",
 [("AI · LLM · RAG","IntelliQuery","Natural-language-to-SQL assistant that lets non-technical users self-serve reliable answers — LLMs, RAG over a semantic layer, and guardrails that keep the SQL safe and grounded.",["LLM","RAG","SQL","Prompt Engineering"],"https://github.com/Bandelasrivigna/IntelliQuery","View code"),
  ("Analytics Engineering","MetricsHub","Single-source-of-truth metrics layer with governed dbt models and BI dashboards, so analysts self-serve consistent KPIs without re-deriving business logic.",["dbt","SQL","Tableau","Power BI","Metrics Layer"],"https://github.com/Bandelasrivigna","GitHub"),
  ("Experimentation","GrowthLab","A/B testing & product-analytics workbench: designs experiments, measures lift with statistical rigor, and turns results into clear recommendations.",["SQL","Python","A/B Testing","Statistics"],"https://github.com/Bandelasrivigna","GitHub")],
 [("Analytics & SQL",["Advanced SQL","CTEs","Window Functions","KPI Analysis","Statistical Analysis","A/B Testing"]),
  ("Visualization & BI",["Tableau","Power BI","Google Data Studio","Advanced Excel","Data Storytelling"]),
  ("Analytics Engineering",["Data Modeling","Semantic Models","dbt","Metrics Layer","Data Quality","Governance"]),
  ("Programming & Cloud",["Python (Pandas, NumPy)","SQL","R","Snowflake","BigQuery","AWS / GCP"])],
 [("Data Analyst / Analytics Engineer — HCL Technologies","Aug 2022 – Jul 2024",
   ["Optimized complex SQL over millions of rows; cut report-refresh times 40%.",
    "Built a data-quality framework with 25+ automated checks, cutting downstream corrections ~60%.",
    "Designed dbt semantic models & BI dashboards translating 15+ sources into trusted KPIs."]),
  ("Associate Software Engineer — ApheX (Startup)","Jul 2021 – Apr 2022",
   ["Built data pipelines & SQL reporting from scratch, owning quality end to end.",
    "Automated recurring reporting, freeing time for analysis."]),
  ("M.S. Computer Science — Governors State University","Aug 2024 – May 2026",
   ["GPA 3.90 · Data Analysis, Statistics, Database Systems."])],
 ["Google Professional Data Engineer","dbt Analytics Engineer","AWS Certified Data Engineer"],
 "Need a single source of truth?")

# ---------- SOFTWARE ENGINEER ----------
page("software-engineer.html","Srivigna Reddy Bandela — Software Engineer",
 "#a06bff","#7b6bff","#31d6c7",
 ["Software Engineer","Full-Stack Developer","Backend Engineer","Systems Builder"],
 ["Open to Software Engineer roles","I design and ship full-stack apps, REST APIs, and cloud-native microservices — clean, tested, scalable code across the whole lifecycle."],
 [("3","+","Years experience"),("30","","Backend tools built"),("90","%","Test coverage"),("3","","Certifications")],
 "Shipping software that scales",
 "Software Engineer with 3 years designing, building, and shipping full-stack and backend applications. Strong in Python, Java, TypeScript, and SQL, with hands-on REST APIs, microservices, and cloud-native services on AWS. Solid CS foundation in data structures, algorithms, system design, and testing — delivering clean, scalable code in Agile teams. Completing an MS in Computer Science (GPA 3.90).",
 [("Full-Stack · AI","IntelliQuery","Full-stack app — React/TypeScript front end, Python/FastAPI backend on AWS — that turns natural language into validated SQL with LLMs and RAG, deployed with REST APIs, auth, and CI/CD.",["React","FastAPI","AWS","REST","LLM"],"https://github.com/Bandelasrivigna/IntelliQuery","View code"),
  ("Backend · Systems","MCP Server","30-tool backend platform exposing REST-style interfaces and tool orchestration across a distributed microservice architecture — schema validation, observability, containerized deployment.",["Python","Microservices","REST","Docker","CI/CD"],"https://github.com/Bandelasrivigna","GitHub"),
  ("Distributed Systems","Real-Time Event Streaming","High-throughput, low-latency service in Java + Kafka with fault-tolerant design, full test coverage, and monitoring for reliable production operation under load.",["Java","Kafka","PostgreSQL","Testing"],"https://github.com/Bandelasrivigna","GitHub")],
 [("Languages",["Python","Java","JavaScript","TypeScript","SQL","C/C++","Unix Shell"]),
  ("Backend & APIs",["REST APIs","GraphQL","Microservices","FastAPI","Node.js","Kafka","Event-Driven"]),
  ("Frontend & Full-Stack",["React","TypeScript","Redux","HTML/CSS","Responsive UI"]),
  ("Cloud, DevOps & CS",["AWS","Docker","Kubernetes","CI/CD","Terraform","Data Structures","System Design"])],
 [("Software Engineer — HCL Technologies","Aug 2022 – Jul 2024",
   ["Shipped full-stack features end to end (React/TS, Python/Java, REST APIs) for enterprise apps.",
    "Built scalable microservices & cloud-native services on AWS with OOP and design patterns.",
    "Drove CI/CD (GitHub Actions), comprehensive tests, and code reviews to raise the quality bar."]),
  ("Associate Software Engineer — ApheX (Startup)","Jul 2021 – Apr 2022",
   ["Architected the startup's first backend services & REST APIs from scratch.",
    "Set up CI/CD, automated testing, and Git workflows for rapid, reliable shipping."]),
  ("M.S. Computer Science — Governors State University","Aug 2024 – May 2026",
   ["GPA 3.90 · Data Structures & Algorithms, System Design, Distributed Systems."])],
 ["AWS Certified Data Engineer","AWS Certified Machine Learning","Google Professional Data Engineer"],
 "Building something that needs to scale?")
