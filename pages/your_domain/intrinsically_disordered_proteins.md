---
title: Intrinsically disordered proteins
description: Data management solutions for intrinsically disordered proteins data.
contributors: [Ivan Mičetić]
related_pages: 
page_id: idp
related_pages: 
  Your_tasks: [metadata]
  Tool_assembly: []
---

## Introduction

Intrinsically disordered proteins (IDP) domain brings together databases and tools needed to organize IDP data and knowledge in a Findable, Accessible, Interoperable and Reusable (FAIR) manner. Experimental data created by users must be complemented by metadata in order to be deposited in an IDP resource. This document describes what community standards must be followed and where to find information needed to complete the metadata of an IDP experiment or study.

## Annotating or curating data from an IDP related experiment or study
 
### Description

As a researcher in the field of Intrinsically Disordered Proteins (IDPs), you want to know how to process an experimental result in a FAIR way. As a final aim, you want to deposit the data in a community database or registry for wider adoption.

### Considerations
You can split the experimental process in several steps:
* How should you properly describe an IDP experiment? Are there any community standards that you should follow?
* How do you add metadata in order to make IDP data more machine readable?
* How should you publish IDP data to a wider audience?

### Solutions
* The IDP community developed a {% tool "miade" %} standard under a PSI-ID workgroup. The standard specifies the minimum information required to comprehend the result of a disorder experiment.

    The standard is available in XML and TAB format. You can check example annotation in [XML](https://github.com/normandavey/HUPO-PSI-ID/blob/master/HUPO-PSI-ID_XML_format_compact_NFAT_example.xml) and [TAB](https://github.com/normandavey/HUPO-PSI-ID/blob/master/HUPO-PSI-ID_TAB_format.xlsx) format and adapt it to your data.
* The IDP community developed the Intrinsically Disordered Proteins Ontology ({% tool "idpo" %}). The ontology is an agreed consensus of terms used in the community, organised in a structured way.

    The ontology is available in [OWL](https://disprot.org/assets/data/idpontology_disprot_8_v0.1.0.owl) and [OBO](https://disprot.org/assets/data/idpontology_disprot_8_v0.1.0.obo) format. 
* You should deposit primary data into relevant community databases ({% tool "bmrb" %}, {% tool "pcddb" %}, {% tool "sasbdb" %}). You should deposit literature data to the manually curated database {% tool "disprot" %}. DisProt is built on MIADE standard and IDPO ontology. As such, DisProt requires curators to annotate all new data according to community standards. IDP data from primary databases, together with curated experimental annotations and software predictions, is integrated in the comprehensive {% tool "mobidb" %} database. DisProt and MobiDB add and expose {% tool "bioschemas" %} markup to all data records increasing data findability and interoperability.

## Issues annotating or describing an IDP related term or study

### Description
IDP field is actively evolving. It integrates newly published experimental evidence of protein disorder and translates it in a machine readable way in an IDP database. This mapping process relies on accurate knowledge of protein identifiers, protein regions under study and disorder region functional annotation.

### Considerations
Most common issues that you as a researcher can encounter during the mapping process are:
* how to properly and uniquely identify the protein (or fragment) under study?
* how to deal with missing terms in IDPO?

### Solutions
* In order to uniquely identify the protein under study, you should identify the protein on {% tool "uniprot" %} reference protein database. The protein identifier must be complemented with an isoform identifier (if needed) in order to completely match the experimental protein sequence.

  Use the {% tool "sifts" %} database to precisely map the experimental protein fragment (deposited at {% tool "pdb" %}) to a reference protein database ({% tool "uniprot" %}) at an amino acid level.
* Experimental evidence from literature must be mapped to relevant IDPO terms. If no suitable term could be found in IDPO, try with following resources:
  * [Evidence & Conclusion Ontology (ECO)](https://www.ebi.ac.uk/ols/ontologies/eco) for experimental methods
  * [Molecular Interactions Controlled Vocabulary](https://www.ebi.ac.uk/ols/ontologies/mi) for molecular interactions
  * [Gene Ontology](https://www.ebi.ac.uk/ols/ontologies/go) for functional terms

  If there isn't an appropriate term in ontologies or vocabularies, you can submit a new proposal for community review at [DisProt feedback](https://disprot.org/feedback).
