---
title: "Intrinsically Disordered Proteins"
---


## Annotating or curating data from an IDP related experiment or study
 
### Description

As a researcher in the field of Intrinsically Disordered Proteins (IDPs), you want to know how to process an experimental result in a FAIR way. As a final aim, you want to deposit the data in a community database or registry for wider adoption.

### Considerations
You can split the experimental process in several steps:
* How should you describe properly an IDP experiment? Are there any community standards that you should follow?
* How do you add metadata in order to make IDP data more machine readable?
* How should you publish IDP data to a wider audience?

### Solutions
* The IDP community developed a [MIADE](http://www.psidev.info/intrinsically-disordered-proteins-workgroup) standard under a PSI-ID workgroup. The standard specifies the minimum information required to comprehend the result of a disorder experiment.

    The standard is available in XML and TAB format. You can check example annotation in [XML](https://github.com/normandavey/HUPO-PSI-ID/blob/master/HUPO-PSI-ID_XML_format_compact_NFAT_example.xml) and [TAB](https://github.com/normandavey/HUPO-PSI-ID/blob/master/HUPO-PSI-ID_TAB_format.xlsx) format and adapt it to your data.
* The IDP community developed an Intrinsically Disordered Proteins Ontology (IDPO). The ontology is an agreed consensus of terms used in the community, organized in a structured way.

    The ontology is available in [OWL](https://disprot.org/assets/data/idpontology_disprot_8_v0.1.0.owl) and [OBO](https://disprot.org/assets/data/idpontology_disprot_8_v0.1.0.obo) format. 
* You should deposit primary data into relevant community databases ([BMRB](http://www.bmrb.wisc.edu/), [PCDDB](https://pcddb.cryst.bbk.ac.uk/), [SASBDB](https://www.sasbdb.org/)). You should deposit literature data to the manually curated database [DisProt](https://disprot.org/). DisProt is built on MIADE standard and IDPO ontology. As such, DisProt requires curators to annotate all new data according to community standards. DisProt adds and exposes [Bioschemas](https://bioschemas.org/) markup to all data records increasing data findability and interoperability.
