---
title: Galaxy
contributors: [Amandine Nunes-Jorge, Beatriz Serrano-Solano]
description: Galaxy is an open, web-based platform for accessible, reproducible, and transparent computational research.
page_id: galaxy
affiliations: [ELIXIR Europe, "European Union"]
related_pages: 
  Your_tasks: [data_analysis, data_organisation, data_publication, data_quality, data_transfer, existing_data, identifiers, machine_actionability, metadata]
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
- **manage data** by sharing and publishing results, workflows, and visualisations;
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

<style>
  #galaxy-rdm .tool {
  white-space: normal !important;
}
</style>
<div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3 g-4" id="galaxy-rdm">
  <div class="col">
    <div class="card border border-3 h-100" style="border-color: #fac54b!important">
    <div style="background-color:#fac54b;">
        <img src="{{ '/images/life_cycle_icons/collect-icon.svg' | relative_url }}" class="card-img-top pt-3" style="max-height: 5em;" alt="collect">
        <h3 class="card-title text-center mb-4 ff-theme mt-0 text-white">Collect</h3>
      </div>
      <div class="card-body">
        <h4 class="mt-0">Access to databases</h4>
        <ul class="lh-sm">
          <li>{% tool "uniprot" %}</li>
          <li><a href="http://intermine.org/">InterMine</a></li>
          <li>{% tool "omero" %}</li>
          <li>{% tool "omicsdi" %}</li>
          <li><a href="https://www.copernicus.eu/en">Copernicus</a></li>
          <li><a href="https://genome.ucsc.edu/">UCSC genome browser</a> (<a href="https://training.galaxyproject.org/training-material/topics/introduction/tutorials/galaxy-intro-strands/tutorial.html">tutorial</a>)</li>
          <li><a href="https://www.ncbi.nlm.nih.gov/datasets/">NCBI datasets</a></li>
          <li>{% tool "international-nucleotide-sequence-database-collaboration" %}</li>
          <li>{% tool "european-nucleotide-archive" %}</li>
          <li>{% tool "pdb" %}</li>
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
  </div>
  <div class="col">
    <div class="card border border-3 h-100" style="border-color: #8aba56!important">
      <div style="background-color:#8aba56;">
        <img src="{{ '/images/life_cycle_icons/process-icon.svg' | relative_url }}" class="card-img-top pt-3" style="max-height: 5em;" alt="process">
        <h3 class="card-title text-center mb-4 ff-theme mt-0 text-white">Process</h3>
      </div>
      <div class="card-body">
        <h4 class="mt-0">Data transformation</h4>
        <ul class="lh-sm">
          <li>Data transformation tools</li>
          <li>Quality control</li>
          <li>Data cleaning</li>
          <li>Annotation</li>
          <li><a href="https://live.usegalaxy.eu/">Interactive Tools</a> (<a href="https://openrefine.org/">OpenRefine</a>, RStudio, Jupyter Notebook)</li>
        </ul>
        <h4>Import workflows</h4>
        <ul class="lh-sm">
          <li>{% tool "workflowhub" %}</li>
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
  </div>
  <div class="col">
    <div class="card border border-3 h-100" style="border-color: #32b890!important">
      <div style="background-color:#32b890;">
        <img src="{{ '/images/life_cycle_icons/analyse-icon.svg' | relative_url }}" class="card-img-top pt-3" style="max-height: 5em;" alt="analyse">
        <h3 class="card-title text-center mb-4 ff-theme mt-0 text-white">Analyse</h3>
      </div>
      <div class="card-body">
        <h4 class="mt-0">2,900 domain-specific tools</h4>
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
  </div>
  <div class="col">
    <div class="card border border-3 h-100" style="border-color: #4176a5!important">
      <div style="background-color:#4176a5;">
        <img src="{{ '/images/life_cycle_icons/preserve-icon.svg' | relative_url }}" class="card-img-top pt-3" style="max-height: 5em;" alt="preserve">
        <h3 class="card-title text-center mb-4 ff-theme mt-0 text-white">Preserve</h3>
      </div>
      <div class="card-body">
        <h4 class="mt-0">Export artefacts</h4>
        <ul class="lh-sm">
          <li>Workflows</li>
          <li>History</li>
          <li>Datasets</li>
        </ul>
        <h4>Formats</h4>
        <ul class="lh-sm">
          <li>Archive file</li>
          <li><a href="https://biocomputeobject.org/">BioCompute Object</a></li>
          <li>{% tool "research-object-crate" %}</li>
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
  </div>
  <div class="col">
    <div class="card border border-3 h-100" style="border-color: #9e51ad!important">
      <div style="background-color:#9e51ad;">
        <img src="{{ '/images/life_cycle_icons/share-icon.svg' | relative_url }}" class="card-img-top pt-3" style="max-height: 5em;" alt="share">
        <h3 class="card-title text-center mb-4 ff-theme mt-0 text-white">Share</h3>
      </div>
      <div class="card-body">
        <h4 class="mt-0">Share artefacts</h4>
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
  </div>
  <div class="col">
    <div class="card border border-3 h-100" style="border-color: #fa484b!important">
      <div style="background-color:#fa484b;">
        <img src="{{ '/images/life_cycle_icons/reuse-icon.svg' | relative_url }}" class="card-img-top pt-3" style="max-height: 5em;" alt="reuse">
        <h3 class="card-title text-center mb-4 ff-theme mt-0 text-white">Reuse</h3>
      </div>
      <div class="card-body">
        <h4 class="mt-0">Account cleaning</h4>
        <ul class="lh-sm">
          <li>Storage dashboard to manage quota</li>
          <li>Bulk (permanent) delete</li>
          <li>Quota temporarily extendable</li>
          <li>Multiple quota per object storage (WIP)</li>
        </ul>
        <h4>Import artefacts</h4>
        <ul class="lh-sm">
          <li>Histories (own, shared by others)</li>
          <li>Workflows from the {% tool "workflowhub" %}</li>
        </ul>
      </div>
    </div>
  </div>
</div>

