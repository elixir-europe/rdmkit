---
title: Creating a data workflow diagram
contributors: [Vilem Ded]
description: Best practices to capture your planned data workflow in a diagram.
page_id: creating_workflow_diagram
---

## How to create a data workflow diagram?

### Description

Creating a data workflow diagram for your research project greatly enhances your data management process.
While [Data Management Plans (DMPs)](data_management_plan) can span tens or even hundreds of pages, a diagram offers a more concise and accessible way to represent your workflow.
This visual approach helps bridge the gap between partners who may have varying perceptions and levels of understanding, ensuring everyone is aligned.
Diagrams make it easier to identify potential issues by highlighting undocumented data sources or destinations that might otherwise go unnoticed in a lengthy document.
A well-crafted workflow diagram also boosts the engagement of less-involved partners or stakeholders, giving them a clear and intuitive way to contribute to the planning process.

### Considerations

* A simple diagram can significantly improve clarity and communication and it's essential to first consider the complexity of the workflow. For complex project with multiple steps, data sources, or stakeholders, a diagram is invaluable for identifying steps, dependencies, potential issues and ensuring everyone has a shared understanding.
* The more complex the workflow, the more time and effort it will take to create and update the diagram. It is important to plan carefully and ensure that the time invested in diagram creation and updates is manageable and that your contribution is clearly recognized.
* A diagram may include sensitive or confidential information or reveal critical details that could be exploited by attackers, such as system vulnerabilities or data access points. Therefore, be cautious about sharing information publicly. Ensure that appropriate security measures are in place and such information is properly protected to prevent security breaches.
* While a diagram is a helpful tool, it is usually not legally binding without a formal, written description of the workflow. It’s good practice to complement your diagram with a full textual annex to ensure the process is well-documented and understood.
* Content of the diagram will depend on many factors. It is good practice to start with definition of the targeted audience (project partners, data managers, funders, public) and main purpose (capturing life of project data, clarification of data protection framework​, description of pre-processing steps). Based on the targeted audience and purpose, you can then more precisely define the scope of your diagram, i.e. what (not) to include. These can be physical assets and entities (partners/people, storage locations, instruments, datasets, documents) or logical elements of your project (processes, data types, partner roles).
* Same as DMPs, the diagram is a living resource and should be updated as the research project progresses.

### Solution

* Start with a simple top level diagram​. Share it and get feedback on what can be refined.

* You can follow these steps.
  1. List all assets.
  2. List all partners and actors​.
  3. List all processes​.
  4. Define data sources​ - such as instrument, patient, collaborator, lab.
  5. Define final data locations (sinks)​ - for example, archives, repositories, external processes, ingestion zones.
  6. Start drawing visual elements representing the outer interface (sources and sinks) and move inwards.
  7. Iteratively refine the diagram based on items which were not yet included.

* Too complex diagrams can be split. Define sub-processes and detect input/output flows or interfaces.
* Various attributes of visual elements can be mapped to aesthetics. These can be:
  * square for process performed automatically vs. rectangle for process performed manually (shape);
  * red line for sensitive data flow vs. blue for non-sensitive data (line color);
  * color, fill, border.
* Be consistent in mapping the of aesthetics. For example, instead of using fill colors to depict encryption status (red vs blue) and collaborator's roles (green for researchers vs blue for contractors), you can use small key icons for the encryption status (shape).
* Include a legend if the aesthetics is complicated.

* Don't forget to include the date of last update, version and your name.

* Source files for the diagrams should be vector based to facilitate portability and reuse. For example, Scalable Vector Graphics (SVG).
* For dissemination, you can use a raster-graphics file format such as Portable Network Graphics (PNG) or other.
* Use a vector graphics tool of your preference.
  * Open source: {% tool "draw-io" %}, {% tool "inkscape" %}, {% tool "libre-office-draw" %}.
  * Licensed: MS Visio, Miro.com, Corel Draw, MS PowerPoint, Affinity Designer or Adobe Illustrator.
* Investigate your tool and all features it provides. E.g. {% tool "draw-io" %} allows you to host the diagram in {% tool "github" %} making it a very convenient tool for collaborative editing.
