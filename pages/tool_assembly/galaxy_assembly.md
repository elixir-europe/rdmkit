---
title: Galaxy
contributors: [Amandine Nunes-Jorge, Beatriz Serrano-Solano]
description: Galaxy is an open, web-based platform for accessible, reproducible, and transparent computational research.
page_id: Galaxy
affiliations: [ELIXIR Europe, "European Union"]
related_pages: 
  your_tasks: [data analysis, data organisation, data publication, data quality, data transfer, existing data, identifiers, machine actionability, metadata]
  your_domain:
training:
  - name: Galaxy Training Network
    url: https://training.galaxyproject.org/
  - name: Galaxy Mentor Network
    url: https://galaxy-mentor-network.netlify.app/
  - name: Training in TeSS
    registry: TeSS
    registry_url: https://tess.elixir-europe.org
    url: https://tess.elixir-europe.org/search?q=galaxy
---

## What is Galaxy?

Galaxy is a well-known **open-source platform for FAIR data analysis** that enables users to:
- **access and collect data** from reference databases, external repositories and other data sources;
- **use tools from various domains** that can be plugged into workflows through its graphical web interface;
- **run code in interactive environments** (RStudio, Jupyter...) along with other tools or workflows;
- **manage data** by sharing and publishing results, workflows, and visualizations;
- **capture the metadata** of data analyses, thus ensuring their reproducibility.

Galaxy supports scientists to perform accessible, reproducible, and transparent computational analysis. The Galaxy Community is actively involved in helping the ecosystem improve and sharing scientific discoveries.

<!-- {% include image.html file="galaxy-rdmkit.png" caption="Figure 1. Uses of Galaxy throughout the whole data life cycle." alt="Galaxy RDMkit" %} -->
## Who can use Galaxy?

Galaxy also provides [open infrastructure ready to use for researchers worldwide](https://galaxyproject.org/use/). All what you need is a web browser and an account in a public server:
- [European Galaxy server](https://usegalaxy.eu/)
- [US Galaxy server](https://usegalaxy.org/)
- [Australian Galaxy server](https://usegalaxy.org.au/)

## What can you use Galaxy for?

Galaxy can be used at different stages of the data life cycle, covering from the data collection to the reuse steps. 

<div class="container-fluid g-0 m-1">
  <div class="row row-cols-1 row-cols-md-3">
      <div class="card mb-4">
        <div class="card-body px-4" style="background-color: #fac54b45">
          <h3 class="card-title text-center mb-4 mt-3">Collect</h3>
          <h4>Access to databases</h4>
          <ul class="lh-sm">
            <li><a href="https://www.uniprot.org/">UniProt</a></li>
            <li><a href="http://intermine.org/">InterMine</a></li>
            <li><a href="https://www.openmicroscopy.org/omero/">OMERO</a></li>
            <li><a href="https://www.omicsdi.org/">OmicsDI</a></li>
            <li><a href="https://www.copernicus.eu/en">Copernicus</a></li>
            <li><a href="https://genome.ucsc.edu/">UCSC genome browser</a> (<a href="https://training.galaxyproject.org/training-material/topics/introduction/tutorials/galaxy-intro-strands/tutorial.html">tutorial</a>)</li>
            <li><a href="https://www.ncbi.nlm.nih.gov/datasets/">NCBI datasets</a></li>
            <li><a href="https://www.insdc.org/">INSDC</a> (<a href="https://www.ebi.ac.uk/ena/browser/about">ENA</a>)</li>
            <li><a href="https://www.rcsb.org/">PDB</a></li>
            <li>3rd-party databases</li>
          </ul>
          <h4>Customised data access</h4>
          <ul class="lh-sm">
            <li>Data libraries</li>
            <li>BYOD (Posix, WebDav, Dropbox, ...)</li>
            <li>On-demand reference data</li>
            <li><i>Deferred</i> data from remote locations</li>
          </ul>
          <h4>LIMS integration</h4>
          <ul class="lh-sm">
            <li>Connect to sequencing facilities</li>
            <li>Rich API for integration with LIMS</li>
          </ul>
        </div>
      </div>
      <div class="card mb-4">
        <div class="card-body px-4" style="background-color: #8aba5645">
          <h3 class="card-title text-center mb-4 mt-3">Process</h3>
          <h4>Data transformation</h4>
          <ul class="lh-sm">
            <li>Data transformation tools</li>
            <li>Quality control</li>
            <li>Data cleaning</li>
            <li>Annotation</li>
            <li><a href="https://live.usegalaxy.eu/">Interactive Tools</a> (<a href="https://openrefine.org/">OpenRefine</a>, RStudio, Jupyter Notebook)</li>
          </ul>
          <h4>Import workflows</h4>
          <ul class="lh-sm">
            <li><a href="https://workflowhub.eu/">WorkflowHub</a></li>
            <li><a href="https://dockstore.org/">Dockstore</a></li>
            <li><a href="https://www.ga4gh.org/news/tool-registry-service-api-enabling-an-interoperable-library-of-genomics-analysis-tools/">GA4GH TRS API</a></li>
          </ul>
          <h4>Metadata handling</h4>
          <ul class="lh-sm">
            <li>Provenance tracking</li>
            <li>Automatic metadata enrichment</li>
            <li>Bulk (meta)data manipulation</li>
          </ul>
        </div>
      </div>
      <div class="card mb-4">
        <div class="card-body px-4" style="background-color: #32b89045">
          <h3 class="card-title text-center mb-4 mt-3">Analyse</h3>
          <h4>2,900 domain-specific tools</h4>
          <ul class="lh-sm">
            <li><a href="https://cancer.usegalaxy.eu/">Cancer research</a></li>
            <li><a href="https://climate.usegalaxy.eu/">Climate science</a></li>
            <li><a href="https://cheminformatics.usegalaxy.eu/">Computational chemistry</a></li>
            <li><a href="https://ecology.usegalaxy.eu/">Ecology</a></li>
            <li><a href="https://assembly.usegalaxy.eu/">Genomics</a></li>
            <li><a href="https://imaging.usegalaxy.eu/">Imaging</a></li>
            <li><a href="https://materials.usegalaxy.eu/">Material science</a></li>
            <li><a href="https://metabolomics.usegalaxy.eu/">Metabolomics</a></li>
            <li><a href="https://microbiome.usegalaxy.eu/">Microbiome</a></li>
            <li><a href="https://ml.usegalaxy.eu/">Machine learning</a></li>
            <li><a href="https://plants.usegalaxy.eu/">Plant biology</a></li>
            <li><a href="https://proteomics.usegalaxy.eu/">Proteomics</a></li>
            <li><a href="https://singlecell.usegalaxy.eu/">Single-cell omics</a></li>
          </ul>
        </div>
      </div>
      <div class="card mb-4">
        <div class="card-body px-4" style="background-color: #4176a545">
          <h3 class="card-title text-center mb-4 mt-3">Preserve</h3>
          <h4>Export artefacts</h4>
          <ul class="lh-sm">
            <li>Workflows</li>
            <li>History</li>
            <li>Datasets</li>
          </ul>
          <h4>Formats</h4>
          <ul class="lh-sm">
            <li>Archive file</li>
            <li><a href="https://biocomputeobject.org/">BioCompute Object</a></li>
            <li><a href="https://www.researchobject.org/ro-crate/">RO-Crate</a> (WIP)</li>
          </ul>
          <h4>Export to remote sources</h4>
          <ul class="lh-sm">
            <li>FTP</li>
            <li>Dropbox</li>
            <li>S3 Bucket</li>
            <li>AWS</li>
            <li>GDrive</li>
            <li>Nextcloud</li>
            <li>WebDav</li>
            <li>Google Cloud Storage</li>
          </ul>
        </div>
      </div>
      <div class="card mb-4">
        <div class="card-body px-4" style="background-color: #9e51ad45">
          <h3 class="card-title text-center mb-4 mt-3">Share</h3>
          <h4>Share artefacts</h4>
          <ul class="lh-sm">
            <li>Datasets</li>
            <li>Histories</li>
            <li>Workflows</li>
            <li>Visualizations</li>
            <li>GA4GH Beacon (WIP)</li>
            <li>DRS server</li>
          </ul>
          <h4>Shareability</h4>
          <ul class="lh-sm">
            <li>RBAC (Role-Based Access Control)</li>
            <ul class="lh-sm">
              <li>One user</li>
              <li>A group of users</li>
              <li>Public</li>
            </ul>
          </ul>
        </div>
      </div>
      <div class="card mb-4">
        <div class="card-body px-4" style="background-color: #fa484b45">
          <h3 class="card-title text-center mb-4 mt-3">Reuse</h3>
          <h4>Account cleaning</h4>
          <ul class="lh-sm">
            <li>Storage dashboard to manage quota</li>
            <li>Bulk (permanent) delete</li>
            <li>Quota temporarily extendable</li>
            <li>Multiple quota per object storage (WIP)</li>
          </ul>
          <h4>Import artefacts</h4>
          <ul class="lh-sm">
            <li>Histories (own, shared by others)</li>
            <li>Workflows from the <a href="https://workflowhub.eu/">WorkflowHub</a></li>
          </ul>
        </div>
      </div>
  </div>
</div>
