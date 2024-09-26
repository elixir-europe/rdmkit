---
title: Data workflow diagram
contributors: [Vilem Ded]
description: Best practices to capture your planned data workflow in a diagram.
page_id: data_workflow_diagram
related_pages: 
dsw:
faircookbook:
---

## Why you should draw a data workflow diagram?

### Description

Creating a data workflow diagram for your research project greatly enhances your data management process. While Data Management Plans (DMPs) can span tens or even hundreds of pages, a diagram offers a more concise and accessible way to represent your workflow. This visual approach helps bridge the gap between partners who may have varying perceptions and levels of understanding, ensuring everyone is aligned. Diagrams make it easier to identify potential issues by highlighting undocumented data sources or destinations that might otherwise go unnoticed in a lengthy document. Additionally, these visual representations are invaluable during discussions and planning sessions, sparking deeper conversations and encouraging collaboration. A well-crafted workflow diagram also boosts the engagement of less-involved partners or stakeholders, giving them a clear and intuitive way to contribute to the planning process.

### Considerations

* Even a simple diagram can significantly improve clarity and communication, but it's essential to first consider the complexity of the workflow. If the process is straightforward and can be easily described in a single paragraph, a diagram might not be necessary. However, for more complex workflows, a diagram is invaluable for identifying steps, dependencies, and potential issues.
* If your workflow can be fully explained in a short, detailed paragraph, then a diagram may not add much value. However, for processes with multiple steps, data sources, or stakeholders, a diagram helps break down complexities and ensures everyone has a shared understanding.
* The more complex the workflow, the more time and effort it will take to create and update the diagram. It’s important to plan carefully and ensure that the time invested in diagram creation and updates is manageable and that your contribution is clearly recognized.
* A diagram can include sensitive or confidential information, so be cautious about sharing it publicly. Ensure that proper security measures are in place if the diagram contains details that should remain private.
* Be aware that diagrams can reveal critical details that could be exploited by attackers, such as system vulnerabilities or data access points. Make sure any workflow diagram that includes sensitive information is properly protected to prevent security breaches.
* While a diagram is a helpful tool, it is usually not legally binding without a formal, written description of the workflow. It’s good practice to complement your diagram with a full textual annex to ensure the process is well-documented and understood.
* Content of the diagram will depend on many factors. Its good practice to start with definition of the targeted audience (project partners, data managers, funders, public) and main purpose (capturing life of project data, clarification of data protection framework​, description of pre-processing steps). Based on the targeted audience and purpose, you can then more precisely define the scope of your diagram, e.i what (not) to include. These can be physical assets and entities (partners/people, storage locations, instruments, datasets, documents) or logical elements of your project (processes, data types, partner roles, ...).
* Same as DMP, the diagram is a living resource and should be updated as the research project progresses.

### Solution

* Start with simple top level diagram​. Share it and get feedback on what can be refined.

* You can follow these steps.
  1. List all assets.
  2. List all partners and actors​.
  3. List all processes​.
  4. Define data sources​ - instrument, patient, collaborator, lab, ...
  5. Define final data locations (sinks)​ - archives, repositories, external processes, ingestion zones, ...
  6. Start drawing visual elements representing the outer interface (sources and sinks) and move inwards.
  7. Iteratively refine the diagram based on items which were not yet included.

* Too complex diagrams can be split. Define sub-processes and detect input/output flows /interface).
* Various attributes of visual elements can be mapped to aesthetics.  These can be:
  * square for processes performed automatically vs. rectangle for processes performed manually (shape).
  * red line for sensitive data flow vs. blue for non-sensitive data (line color).
  * color, fill, border, ...​
* Be consistent in mapping of aesthetics. For example, instead of using fill colors to depict encryption status (red vs blue) and collaborator's roles (green for researchers vs blue for contractors), you can use small key icon for the encryption status (shape).
* Include legend if the aesthetics is complicated
* If the mapping gets too complicated, include a legend.
* Don't forget to include date of last update, version and your name.

* Source files for the diagrams should be vector based to facilitate portability and reuse. SVG
* For dissemination, you can use PNG or other
* Use vector graphics tool of your preference.
  * open source: Draw.io, Inkscape, Libre Office Draw, ...
  * licensed: MS Visio*, Miro.com*,Corel Draw*, MS PowerPoint*
* Investigate your tool and all features it provides. E.g. Draw.io allows you to host the diagram in Github making it very convenient tool for collaborative editing.
