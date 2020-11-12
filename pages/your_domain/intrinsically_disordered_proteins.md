---
title: "Intrinsically Disordered Proteins community"
---


## "Annotating or curating data from an IDP related experiment or study"
 
### Description

A researcher in the field would like to know how to process an IDP experimental result in a FAIR way with the final aim of depositing the data in a community database or registry.

### Considerations
The process can be separated in several steps:
* Decide how to describe the experiment: what standards should be followed?
* How to add metadata to IDP research data?
* How to publish IDP data to a wider audience?

### Solutions
* IDP community developed a [MIADE](http://www.psidev.info/intrinsically-disordered-proteins-workgroup) standard under a PSI-ID workgroup.
  * Available as XML and TAB format. Example annotation in [XML](https://github.com/normandavey/HUPO-PSI-ID/blob/master/HUPO-PSI-ID_XML_format_compact_NFAT_example.xml) and [TAB](https://github.com/normandavey/HUPO-PSI-ID/blob/master/HUPO-PSI-ID_TAB_format.xlsx) format.
* IDP community is developing an Intrinsically Disordered Proteins Ontology (IDPO)
  * Available as [OWL](https://disprot.org/assets/data/idpontology_disprot_8_v0.1.0.owl) and [OBO](https://disprot.org/assets/data/idpontology_disprot_8_v0.1.0.obo) format.
* Primary data should be deposited to relevant community databases ([BMRB](http://www.bmrb.wisc.edu/), [PCDDB](https://pcddb.cryst.bbk.ac.uk/), [SASBDB](https://www.sasbdb.org/)) while literature data should be deposited to the manually curated database [DisProt](https://disprot.org/) which relies on MIADE standard and IDPO ontology. DisProt adds [Bioschemas](https://bioschemas.org/) markup to all data records increasing data findability and interoperability.
