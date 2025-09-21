[![Dynamic DevOps Roadmap](https://img.shields.io/badge/Dynamic_DevOps_Roadmap-559e11?style=for-the-badge&logo=Vercel&logoColor=white)](https://devopsroadmap.io/getting-started/)
[![Community](https://img.shields.io/badge/Join_Community-%23FF6719?style=for-the-badge&logo=substack&logoColor=white)](https://newsletter.devopsroadmap.io/subscribe)
[![Telegram Group](https://img.shields.io/badge/Telegram_Group-%232ca5e0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/DevOpsHive/985)
[![Fork on GitHub](https://img.shields.io/badge/Fork_On_GitHub-%2336465D?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork)

[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/Jarvis-Ank/devops-hands-on-project-hivebox/badge)](https://scorecard.dev/viewer/?uri=github.com/Jarvis-Ank/devops-hands-on-project-hivebox)

# HiveBox - DevOps End-to-End Hands-On Project

<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox" style="display: block; padding: .5em 0; text-align: center;">
    <img alt="HiveBox - DevOps End-to-End Hands-On Project" border="0" width="90%" src="https://devopsroadmap.io/img/projects/hivebox-devops-end-to-end-project.png" />
  </a>
</p>

> [!CAUTION]
> **[Fork](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork)** this repo, and create PRs in your fork, **NOT** in this repo!

> [!TIP]
> If you are looking for the full roadmap, including this project, go back to the [getting started](https://devopsroadmap.io/getting-started) page.

This repository is the starting point for [HiveBox](https://devopsroadmap.io/projects/hivebox/), the end-to-end hands-on project.

You can fork this repository and start implementing the [HiveBox](https://devopsroadmap.io/projects/hivebox/) project. HiveBox project follows the same Dynamic MVP-style mindset used in the [roadmap](https://devopsroadmap.io/).

The project aims to cover the whole Software Development Life Cycle (SDLC). That means each phase will cover all aspects of DevOps, such as planning, coding, containers, testing, continuous integration, continuous delivery, infrastructure, etc.

Happy DevOpsing ♾️

## Before you start

Here is a pre-start checklist:

- ⭐ <a target="_blank" href="https://github.com/DevOpsHiveHQ/dynamic-devops-roadmap">Star the **roadmap** repo</a> on GitHub for better visibility.
- ✉️ <a target="_blank" href="https://newsletter.devopsroadmap.io/subscribe">Join the community</a> for the project community activities, which include mentorship, job posting, online meetings, workshops, career tips and tricks, and more.
- 🌐 <a target="_blank" href="https://t.me/DevOpsHive/985">Join the Telegram group</a> for interactive communication.

## Preparation

- [Create GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) (if you don't have one), then [fork this repository](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork) and start from there.
- [Create GitHub project board](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project) for this repository (use `Kanban` template).
- Each phase should be presented as a pull request against the `main` branch. Don’t push directly to the main branch!
- Document as you go. Always assume that someone else will read your project at any phase.
- You can get senseBox IDs by checking the [openSenseMap](https://opensensemap.org/) website. Use 3 senseBox IDs close to each other (you can use the following [5eba5fbad46fb8001b799786](https://opensensemap.org/explore/5eba5fbad46fb8001b799786), [5c21ff8f919bf8001adf2488](https://opensensemap.org/explore/5c21ff8f919bf8001adf2488), and [5ade1acf223bd80019a1011c](https://opensensemap.org/explore/5ade1acf223bd80019a1011c)). Just copy the IDs, you will need them in the next steps.

<br/>
<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox/" imageanchor="1">
    <img src="https://img.shields.io/badge/Get_Started_Now-559e11?style=for-the-badge&logo=Vercel&logoColor=white" />
  </a><br/>
</p>

---

## Implementation
<details>
<summary>
    <b>  Phase 1 - Completion Date 9/16/2025 </b> </summary>

<br>

1. Github Account ✅
2. Forked Hivebox Project ✅ 
3. Created Kanban Project Board ✅
4. Created Issues (3 Phases for now) ✅

> Note: Project is Universal, Issues need to be enabled in repos settings > features to create ne issues once project is linked.
</details>

<details>
<summary>
    <b> Phase 2 - Completion Date 9/17/2025 </b>
</summary>

<br>

1. Initial version of HiveBox App (ie prints version) created.
2. Created Dockerfile, python slim used.
3. Docker need to be enabled before buildiing.
4. Build and Run Docker (```docker build -t hivebox:0.0.1 .``` and ```docker run hivebox:0.0.1```)
5. Added simple shell test file under ```Tests/phase2_test.sh``` run it in terminal via ```bash Tests/phase2_test.sh```
6. git initialized locally and pulled from main branch. 


</details>
<details>
<summary>
    <b> Phase 3 - Completion Date 9/20/2025 </b>
</summary>
<br>

1. Pylint and Hadolint used for linting the code and dockerfile.
2. OpenSenseMap API seems to be not working as expected, hence used different API from ```https://open-meteo.com/``` works similar to open sense.
3. Changes done specific to Openmeto API, used average temperature from 3 locations instead of the sensbox average temperature
4. Added ```/version``` and ```/temperature``` endpoints.
5. Containerized using docker.
6. Restructured the folders and files, added ```requirements```, ```.gitignore```, ```.dockerignore```, ```LICENSE``` etc.
7. Created github workflow [```ci.yml```], linting for dockerfile, and code, build and test.
8. Setup [OpenSSF Scorecard](https://securityscorecards.dev/#using-the-github-action) and fixed few possible issues. Since this project only have one active maintainer and few issues can only be resolved if a team is there like the code review which a single user can't do.

> Phase -3 took a good amount of time to complete as fixing the pipeline till it worked first time. One issue faced during pipeline fixing was api ```/temperature``` endpoint specifically giving 500 Error, this seems to be an issue with the endpoint calling outside url of open-meto, for now this has been bypassed. More fixes and improvements will be done as progress towards next phases.

