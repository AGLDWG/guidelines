#### [Australian Government Linked Data Working Group](http://www.linked.data.gov.au)

# URI Guidelines v2.0
#### August 20 2018
##### Authored by Nicholas Car\* and edited by members of the AGLDWG's *Recommendations* subgroup\*\*.
\* <nicholas.car@csiro.au>  
** [www.linked.data.gov.au/contact](http://www.linked.data.gov.au/contact)

## Preface
This document describes how the Australian Government Linked Data Working Group (AGLDWG) assess requests for and allocates persistent URIs for Linked Data dataset, definitional resources and registers. It builds on both international public sector Linked Data URI allocation guidance, such as the United Kingdom's "Designing URI Sets for the UK Public Sector" [[CAB-2010](#ref-CAB-2010)], and the AGLDWG's own 5+ year's experience with persistent URI allocation.

*This document is a second and very different version of the* Guidelines *produced by the Australian Government Linked Data Working Group (AGLDWG). See *[the guidelines repository](https://github.com/AGLDWG/guidelines) *for previous versions.*

For further context around this document and it's use, please see the AGLDWG's *Governance* web page:

* [www.linked.data.gov.au/governance](http://www.linked.data.gov.au/governance)

## Table of Contents
1. [Conformance](#Conformance)
2. [Introduction](#Introduction)
3. [Persistent domain](#PersistentDomain)
4. [URI Registration](#PIDURIRegistration)
5. [Resource Types](#ResourceTypes)
6. [Datasets](#Datasets)
7. [Definitional Resources](#Definitional)
8. [Top-Level Registers](#TopLevelRegisters)
9. [Second-Level Registers](#SecondLevelRegisters)
10. [References](#References)
11. [Appendix A: Resource Linked Data requirements](#app-a)
12. [Appendix B: Resource catalogue item metadata](#app-b)

## 1. <a id="Conformance"></a> Conformance
The key words *MUST*, *MUST NOT*, *REQUIRED*, *SHOULD*, *SHOULD NOT*, *RECOMMENDED*, *MAY*, and *OPTIONAL* in this document are to be interpreted as defined in [[IETF-1997](#ref-IETF-1997)].

Roles associated with this catalogue acting as a 'Metadata Registry', *Overall Registration Authority*, *Registrar*, *Executive Committee*, *Control Committee*, *Overall Stewardship Organization*, *Steward*, *Overall Submitting Organization*, *Submitter*, *All others*, *Read-only user*, are to be interpreted as defined in [[ISO-2015](#ref-ISO-2015)].

URI patterns are expressed using Augmented Backus-Naur Form, as defined in [[IETF-2008](#ref-IETF-2008)].

Status codes used for resources in the PID Allocations Catalogue of *accepted*, *deprecated*, *retired*, *valid*, *experimental*, *stable*, *not accepted*, *invalid*, *reserved*, *superseded*, *submitted*,  are taken from the Registry Ontology [[REY-2012](#ref-REY-2012)] and are re-presented by the AGLDWG as a Linked Data vocabulary at [[AGLDWG-2018b](#ref-AGLDWG-2018b)].

## 2. <a id="Introduction"></a>Introduction    
Government published, public sector information (PSI), usually about the things agencies are responsible for, is intended to be re-used by many, perhaps initially unknown, applications over time. This is to maximise its value to the nation and this aim is communicated in many places, such as the Productivity Commission's "Data Availability and Use" report of 2017 [[PC-2017](#ref-PC-2017)]. For this reason, it is important that elements PSI are able to be identified and accessed in consistent ways for long periods, perhaps multiple decades.

Government departments and agencies often assign identifiers to many digital PSI things and non-public information resources they are responsible for - e.g. datasets, classification concepts, hospitals, equipment, client interactions. These identifiers are then used when referring to or making statements about particular things. For example, when referring to a road closure, the identifier (e.g. "M5") will be used to inform the public or when referring to a particular census Mesh Block, its Australian bureau of Statistics-issued identifier, perhaps "80006300000" will be used. These identifiers might be well known but are most often not actionable, i.e. they cannot be easily used to discover information about the thing they identify, even if it exists, in standard ways.

The Australian Government Linked Data Working Group (AGLDWG) advocates the use of Linked Data [[W3C-2018](#ref-W3C-2018)] as a particular set of technologies to be used for Internet-distributed, machine-readable data and, due to this, advocates the use of Uniform Resource Identifiers (URIs) as identifiers for things. The use of URIs as item identifiers greatly improves their accessibility and can also improve their endurance.

### 2.1 Uniform Resource Locators (URIs)
Linked Data uses URIs which are part of a single, global, identification system used on the World Wide Web, similar to telephone numbers in a public switched telephone network. We are all familiar with URIs at work due to their use for addresses in browsers for web pages. URIs are a key technology supporting Linked Data offering a generic, universal and infinitely expandable mechanism to identify *things*. In order to publish data in a Linked Data fashion, government needs to represent the identifiers they use for things using URIs.

Sir Tim Berners-Lee, who created many aspects of the World Wide Web we now take for granted, defined principles for the use of URIs with Linked Data [[TBL-2009](#ref-TBL-2006)]. This document builds on those principles which, summarised, are:

#### 2.1.1. Use HTTP URIs
Addressing two of the four principles, *'use URIs'* and *'use HTTP URIs', *governments and their agencies publishing Linked Data ***MUST*** provide HTTP URIs as identifiers for resources, in order to support reuse and data integration/linking on the Web in a Linked Data fashion. HTTP URIs enable URIs to be "looked-up" or "dereferenced", which in turn provides access, via a Web browser, to  representations of the resource identified by these URIs.

#### 2.1.2. Provide a machine-readable representation of the resource identified by the URI
In order to enable HTTP URIs to be "dereferenceable", data publishers have to set up the necessary infrastructure (e.g. DNS & HTTP servers) to serve representations or descriptions of resources (e.g. a human-readable HTML representation or a machine-readable RDF/XML representation). For a resource to be considered Linked data, a publisher ***MUST*** publish it using RDF and ***MUST*** publish at least one machine-readable representation of it (e.g. RDF/XML, JSON-LD, Turtle) via the HTTP URI identifying the resource.

Requirement | Description | Conformance
---|---|---
<a id="req-1"></a>[Req 1] | Use HTTP URIs for Linked Data resources | ***MUST***
<a id="req-2"></a>[Req 2] | Provide at least one machine-readable representation in RDF at a resource's URI. | ***MUST***

#### 2.1.3 URI persistence
Much though has gone into ensuring that URIs for things can be made to keep working for a long time, starting with their technical design to avoid specific technology dependence (addressed by [[TBL-2009](#ref-TBL-2006)] and for Linked Data use in [[W3C-2008](#ref-W3C-2008)]) and extending to the governance arrangements for them to avoid, or at least make more resilient, their social systems dependence. Principles for successful persistent identifier generation are articulated in papers such as "The challenge of ensuring persistency of identifier systems" [[CAR-2017](#ref-CAR2-17)] which, among other things, advocates for the use of organisationally-independent identifiers.

Beyond confirming adherence to these principles, the AGLDWG provides instruction on how to create URIs for certain kinds of resources according to URI construction best practice [[W3C-2012](#ref-W3C-2012)] and also provides an individual government organisation-independent namespace for them to use: `linked.data.gov.au`. This namespace, an internet domain, is managed by the AGLDWG.

## 3. <a id="PersistentDomain"></a>Persistent Domain
The AGLDWG has dedicated the URI domain `linked.data.gov.au` to persistent identifiers (PIDs) for Linked Data resources. This is to be able to supply infinitely many PID URIs using a domain that is not coupled to a particular agency's name or function as such domains, for example `dfat.gov.au` which is coupled to the Department of Foreign Affairs and Trade (DFAT), change over time and are thus not persistent. The use of `linked.data.gov.au` is protected by a Memorandum of Understanding signed by the managing agency, the Digital Transformation Agency and 5 agencies interested in Linked Data [[AGLDWG-2018](#ref-AGLDWG-2018)] which came into effect in May, 2018. The MoU requires any proposed changes to the management or use of the domain to be mooted amongst the MoUs signatories.

Requirement | Description | Conformance
---|---|---
<a id="req-3"></a>[Req 3] | Use the domain `linked.data.gov.au` for organisation-independent, Linked Data HTTP URIs | ***MUST***

While the AGLDWG can assist with HTTP URIs generally, they will only assist with the management of those within this domain.

The AGLDWG maintains a public catalogue of requests for PID URIs within `linked.data.gov.au` and of the statuses of those requests (e.g. *submitted*, *accepted*, *invalid* etc.). The "PID Allocations Catalogue" is online at:

* [catalogue.linked.data.gov.au](http://catalogue.linked.data.gov.au)

### 3.1 Previously used domains
The AGLDWG maintains two legacy persistent domains:

1. `environment.data.gov.au`
2. `reference.data.gov.au`

These two domains contains persistent identifiers minted in 2013 - 2018. Resources allocated PID URIs within them appear in the resource catalogue ([catalogue.linked.data.gov.au](http://catalogue.linked.data.gov.au)) and will be maintained indefinitely however no new PID URIs will be allocated using these legacy domains.

### 3.1 Test domain
The AGLDWG maintains a dedicated testing domain, `test.linked.data.gov.au`. *Submitting Organizations* (see role definition below) may request use of this domain to test PID URIs before seeing a PID URI allocation for a resource.

### 3.2 Other domains
The AGLDWG maintains further subdomains of `linked.data.gov.au` for operational reasons such as website hosting (`www.linked.data.gov.au`) and resource cataloguing (`catalogue.linked.data.gov.au`). These domains, while maintained by the AGLDWG are not to be considered persistent.

## 4. <a id="PIDURIRegistration"></a>PID URI Registration
Due to the central management by the AGLDWG of the `linked.data.gov.au` resource and its requirement to be shared among many agencies, PID URIs allocated using it need to be registered to avoid collisions (agencies wanting the same URIs for different things) and also anonymous orphans (PID URIs once registered which become non-functional and for which ownership information is lost). Previous approaches to PID URI allocation by the AGLDWG that did not require registration resulted in ungoverned URIs.

The AGLDWG notes item registration is both commonplace for shared government resources (viz. registration of datasets within [data.gov.au](https:data.gov.au)) and also for URI-based identifiers (viz. [purl.org](http://purl.org) and [w3id.org](https://w3id.org/)).

The AGLDWG requires all allocated PID URIs to be registered with the group and provides guidance below on what types of URIs may be registered, and the process for registration including information required from registrants.

Registration processes (Section 6.2, 7.2 & 8.2 below), follow those of ISO/IEC 11179 [[ISO-2015](#ref-ISO-2015)] with registration of a resource catalogue entry needing to be assigned an approval status of *accepted* (see Section 4.3) being the necessary and sufficient criteria for PID URI allocation for that resource.

### 4.1 Registration roles
The AGLDWG as a whole plays the roles of *Overall Registration Authority* and also *Overall Stewardship Organization*. The Recommendations subgroup of the AGLDWG plays the role of *Registrar* & *Executive Committee*. The Solutions subgroup of the AGLDWG plays the role of *Control Committee* and also *Steward*. See [www.linked.data.gov.au/groups](http://www.linked.data.gov.au/groups) for more information about AGLDWG structure.

Government entities requesting PID URIs play the role of *Overall Submitting Organization* and individuals or groups within those entities submitting specific resources play the role of *Submitter*. Only AGLDWG members may act as an *Overall Submitting Organization*. See [www.linked.data.gov.au/join](http://www.linked.data.gov.au/join) for more information about joining the AGLDWG.

The AGLDWG sees members of any organisation without roles defined above and members of the general public as playing the role of *Read-only user* in that all AGLDWG registers and metadata are freely available and able to be read in a read-only fashion.

AGLDWG groups and related parties and the ISO11179 roles assigned to them described above are summarised in the Table 1.

**Table 1**: AGLDWG groups and related parties and the ISO11179 roles assigned to them  

Group | Role
---|---
AGLDWG | *Overall Registration Authority*, *Overall Stewardship Organization*
Recommendations Subgroup | *Registrar*, *Executive Committee*
Solutions Subgroup | *Control Committee* and also *Steward*
Government entities, members of the AGLDWG | *Overall Submitting Organization*
Members of above requesting PID URIs | *Submitter*
Everyone not listed above | *Read-only user*

### 4.2 Registration workflow
The processing of items for which PID URIs are requested follows workflows. The general workflow for item processing is given in Figure 1.

![](workflow-approval.png)  
**Figure 1**: Workflow diagram showing the general workflow for the approval processing of PID URI allocation requests. Approval statuses are marked.

A more detailed workflow for resource review is given in Figure 2.

![](workflow-review.png)  
**Figure 2**: Workflow diagram showing detailed steps within the resource review workflow. Approval statuses are marked.

A more detailed workflow showing PID URI implementation is given in Figure 3.

![](workflow-implementation.png)  
**Figure 3**: Workflow diagram showing detailed steps within the PID URI implementation workflow. Approval statuses are marked.

Notes on specific workflows per resource type are given below in Sections 6 - 9.

Requirement | Description | Conformance
---|---|---
<a id="req-4"></a>[Req 4] | Submitters requesting PID URIs must follow the AGLDWG's PID URI allocation workflows and submit their requests to the PID Allocations Catalogue | ***MUST***

### 4.3 Approval status
An item's acceptance for PID allocation is indicated with a *status*, terms for which are taken from the Registry Ontology's status vocabulary. The original publication of this vocabulary is [[REY-2012](#ref-REY-2012)] and the AGLDWG has republished it at [[AGLDWG-2018b](#ref-AGLDWG-2018)]) to enable better visibility. The status vocabulary term hierarchy is:

* [accepted](http://linked.data.gov.au/def/status/accepted)
  * [deprecated](http://linked.data.gov.au/def/status/deprecated)
    * [retired](http://linked.data.gov.au/def/status/retired)
    * [superseded](http://linked.data.gov.au/def/status/superseded)
  * [valid](http://linked.data.gov.au/def/status/valid)
    * [experimental](http://linked.data.gov.au/def/status/experimental)
    * [stable](http://linked.data.gov.au/def/status/stable)
* [not accepted](http://linked.data.gov.au/def/status/notAccepted)
  * [invalid](http://linked.data.gov.au/def/status/invalid)
  * [reserved](http://linked.data.gov.au/def/status/reserved)
  * [submitted](http://linked.data.gov.au/def/status/submitted)

 A general state diagram of resources' statuses is given in Figure 4 below.

![](status-states.png)
**Figure 4**: State diagram showing status states of a resource and actions causing state change.  

Following Figure 4, it can be seen that minimal successful path for a resource from first PID URI request to operational implementation is:

`submitted -> accepted -> stable`


## 5. <a id="ResourceTypes"></a>Resource Types
Presently the AGLDWG recognises four types of items for which PID URIs may be requested:

1. Dataset
2. Definitional Resource
3. Top-Level Register
4. Second-Level Register

More types of items may be added in the future. Such an addition will require this document to be updated.

URIs for Datasets are created within the *Dataset Register*, for definitional resources within the *Def Register* and for Top-Level Register items within the *Top-Level Register*. This Top-Level Register contains both the Dataset Register and the Def Register as subregisters. Second-Level Register items are created as registers within individual Datasets or as modules within Top-Level Registers, as detailed in [Section 9](#9-second-level-register-uris).

The next four sections of this document describe how URIs for these four classes of items are formulated and the processes to apply for them.


## 6. <a id="Datasets"></a>Datasets
Dataset can have URIs that identify the dataset as a whole. These URIs are somewhat analogous to the URIs used to indicate datasets in the [data.gov.au](https://data.gov.au) catalogue (e.g. <https://data.gov.au/dataset/rottnest-ferries-underway-temperature> indicating the "Rottnest Ferries Underway Temperature" dataset) but they have more requirements placed on them in order to perform more functions. Where URIs for datasets in `data.gov.au` resolve to a landing page about the dataset and give access to its metadata and links to distributions of it, `linked.data.gov.au` dataset URIs both link to metadata and also act as a top-level register for items within the dataset. Additionally, `linked.data.gov.au` dataset URIs are dataset-specific namespace domains which can be used to create unique URIs for sub-dataset items. For example, a Linked Data version of the "Rottnest Ferries Underway Temperature" dataset could have a URI for each temperature observation which, if delivered at `linked.data.gov.au`, could be something like `https://data.gov.au/dataset/rottnest-ferries-underway-temperature/observation/0026` for an *observation* identified by *0026*.

Dataset producers are free to choose the form that their sub-dataset item URIs take (so-called *hash* or *slash* URIs (see [[W3C-2016](#ref-W3C-2016)]) however they must deliver both the top-level register of their dataset and all visible  subcomponents of it according to Linked Data principles.

Requirement | Description | Conformance
---|---|---
<a id="req-5"></a>[Req 5] | Resources identified using PID URIs must contain only Linked Data and must pass the conformance tests specified for that resource type | ***MUST***

The tests for what constitutes Linked Data and thus a Linked Data dataset are articulated in [Appendix A](#app-a).

### 6.1 Dataset PID URI pattern
The pattern for Dataset PID URIs is:

```
dataset-uri ::=  protocol "://linked.data.gov.au/dataset/" dataset-id
protocol ::= "http" | "https"
dataset-id ::= *(ALPHA | DIGIT | "-")
```

Where `dataset-id` is a shortened form of the dataset title.

An example is that a Linked Data dataset titled "Geocoded National Address File" (G-NAF) could use the `dataset-id` of "gnaf" and thus make the `dataset-uri` of:

`http://linked.data.gov.au/dataset/gnaf`

Subelements of the dataset may have URIs generated with the following pattern:

```
dataset-subelement-uri ::=  dataset-uri hash-or-slash subelement-path
hash-or-slash ::= "#" | "/"
subelement-path ::= subelement-hash-id | class-path subelement-slash-id
subelement-hash-id = *(ALPHA | DIGIT | "-")
class-path ::= *(ALPHA | DIGIT | "-" | "/")
subelement-slash-id ::= *(ALPHA | DIGIT | "-")
```

Where the "gnaf" dataset, using hash URIs for Address subelements "GA1234" could make a `dataset-subelement-uri` of:

`http://linked.data.gov.au/dataset/gnaf#GA1234`

Where the "gnaf" dataset, using slash URIs for Address subelement "GA1234" could make  `dataset-subelement-uri` of:

`http://linked.data.gov.au/dataset/gnaf/address/GA1234`

### 6.2 Registration Process
This process follows the general process as outlined in Figure 1.

* *Submitter* must be eligible, as per Req 6
  * *Submitter* initiates a requests a PID URI allocation for a dataset URI by creating a complete catalogue record in the AGLDWG LD Resource Catalogue
  * the resource type must be set to 'dataset'
  * request approval status to `submitted`
* *Controlling Committee* is automatically notified to review the requests by the catalogue
* *Controlling Committee* reviews the request and approves it if it passes the metadata and Linked Data tests for a dataset described in [Appendix B](#app-b) and [Appendix A](#app-a), respectively
  * if approved, request approval status to `approved`
  * if not approved, resource status set to `not approved`
  * *Submitter* automatically notified of status change
* if approved, *Steward* implements a URI redirect to the hosted dataset and tests implementation
  * if no collisions with existing patterns are found:
    * if the resource is ready, approval status to `stable`
    * if the resource is not ready, else approval status set to `reserved`
  * if collisions are found, approval status set to `invalid`
  * *Submitter* notified
* *Submitting Organization* is free to use allocated URIs

In the event of more than one request for the same `dataset-id`, application precedent wins, so the first application for a particular `dataset-id`, if successful, will be awarded it. Precedents is determined by date of application lodgement, not date of application completion. This is also true for other resource types for their respective IDs.

Requirement | Description | Conformance
---|---|---
<a id="req-6"></a>[Req 6] | For a particular PID URI to be allocated, the request for that allocation must be the first request for it that is subsequently found eligible | ***MUST***


### 6.3 Required Metadata
Metadata to be supplied for the registration of a Linked Data dataset, and thus the allocation of a URI for it, must constitute a valid record for a dataset within the AGLDWG LD Resource Catalogue. Record validity is determined using the process outlined in [Appendix B](#app-b).

Entries in the AGLDWG LD Resource Catalogue are public from submission onwards.


## 7. <a id="Definitional"></a>Definitional Resources
Definitional Resources are Linked Data vocabularies, vocabulary terms, ontologies, ontology terms and potentially other, Linked Data, data model items. Currently, as per Datasets, URI patterning is provided by the AGLDWG at the whole-of-resource level (i.e. whole ontology or whole vocabulary) with URIs for subcomponents such as vocabulary terms or ontology class definitions to be implemented by the definitional resource managers, at their discretion.

### 7.1 Definitional resource PID URI pattern
The pattern for Definitional PID URIs is:

```
definitional-uri ::=  protocol "://linked.data.gov.au/def/" definitional-id
protocol ::= "http" | "https"
definitional-id ::= *(ALPHA | DIGIT | "-")
```

Where `definitional-id` is a shortened form of the definitional resource's title.

An example is that an ontology used to deliver content for a Linked Data implementation of the "Geocoded National Address File" (G-NAF) could use the `definitional-id` of "gnaf" and thus make the `definitional-uri` of:

`http://linked.data.gov.au/def/gnaf`

Another example is that a vocabulary established listing all the types of citizenship status of people in Australia titled "Citizenship Status" could use the `definitional-id` of "citstatus" and thus make the `definitional-uri` of:

`http://linked.data.gov.au/def/citstatus`

Subelements of the definitional resources may have URIs generated with the following pattern:

```
definitional-subelement-uri ::=  definitional-uri hash-or-slash subelement-path
hash-or-slash ::= "#" | "/"
subelement-path ::= subelement-hash-id | class-path subelement-slash-id
subelement-hash-id = *(ALPHA | DIGIT | "-")
class-path ::= *(ALPHA | DIGIT | "-" | "/")
subelement-slash-id ::= *(ALPHA | DIGIT | "-")
```

Where the "gnaf" ontology, using hash URIs could make a `definitional-subelement-uri` for an `Address` class of:

`http://linked.data.gov.au/def/gnaf#Address`

Where the "gnaf" ontology, using slash URIs for `StreetType` codes could make a `definitional-subelement-uri` for the street type `Avenue` of:

`http://linked.data.gov.au/def/gnaf/Avenue`

or, if the `StreetType` codes were modularised within the ontology perhaps:

`http://linked.data.gov.au/def/gnaf/code/StreetTypes/Avenue`

### 7.2 Registration Process
This process follows the general process as outlined in Figure 1.

* *Submitter* must be eligible, as per Req 6
  * *Submitter* initiates a requests a PID URI allocation for a dataset URI by creating a complete catalogue record in the AGLDWG LD Resource Catalogue
  * the resource type must be set to 'definitional'
  * request approval status to `submitted`
* *Controlling Committee* is automatically notified to review the requests by the catalogue
* *Controlling Committee* reviews the request and approves it if it passes the metadata and Linked Data tests for a dataset described in [Appendix B](#app-b) and [Appendix A](#app-a), respectively
  * if approved, request approval status to `approved`
  * if not approved, resource status set to `not approved`
  * *Submitter* automatically notified of status change
* if approved, *Steward* implements a URI redirect to the hosted dataset and tests implementation
  * if no collisions with existing patterns are found:
    * if the resource is ready, approval status to `stable`
    * if the resource is not ready, else approval status set to `reserved`
  * if collisions are found, approval status set to `invalid`
  * *Submitter* notified
* *Submitting Organization* is free to use allocated URIs

### 7.3 Required Metadata
Metadata to be supplied for the registration of a Linked Data defenitional resource, and thus the allocation of a URI for it, must constitute a valid record for such within the AGLDWG LD Resource Catalogue. Record validity is determined using the process outlined in [Appendix B](#app-b).

Entries in the AGLDWG LD Resource Catalogue are public from submission onwards.


## 8. <a id="TopLevelRegisters"></a>Top-Level Register URIs
Top-Level Registers are an index of individual Linked Data objects, promoted to the 'top' of `linked.data.gov.au` for high visibility. Such registers formulated using very basic information - the identity of the register itself (given via its URI), metadata according to the Registry Ontology [[17](#ref-17)] listing the class(es) of items within it and potentially Registry Ontology links to sub pages of the register. lists of particular classes of LD objects that both allow shorter URI allocation than URIs from datasets and also allow items within them to not use URIs deriving from them. As with datasets and definitional resources registered with the AGLDWG for URI allocation, top-level registers require metadata to be lodged so that the content and ownership of the register is known and can be managed.

Since top-level registers are designed to promote and aggregate assessed in order to determine the appropriateness of the requested URI to the class(es) of objects to be listed in the register.

A simple example:

A *Submitting Organization* wishes to have a URI allocated for a top-level register of items of class *widget* and requests `linked.data.gov.au/widget/`. First the *Submitting Organization* will have to have published at least one dataset containing *widgets*, perhaps `linked.data.gov.au/dataset/ds1` containing the (second-level) register `linked.data.gov.au/dataset/ds1/widget/`. The AGLDWG will check that no `widget/` top-level register already exists and, if not, determine if the path segment `widget/` is a fair representation of the items to be listed in that register. Fairness could stem from the name 'widget' approximating the class identity of the items in the register and a minimal chance of the path segment leading users to understand some meaning other than that intended by the *Submitting Organization*, perhaps as a result of commonly used terms in the LD community.

A more complex example about inappropriate naming:

A *Submitting Organization*  wishes to allocate `linked.data.gov.au/service/` for a collection of government services to members of the public. The *Submitting Organization* has published a dataset containing a register of items of class `srv:Service` where 'srv' is a government business ontology. Here the AGLDWG cannot easily approve the request given the generic nature of 'service' which could easily be misconstrued by a user; perhaps they expect a register of Web Service objects.

A federated register example:

A *Submitting Organization*, in this case the Royal Australian Navy (RAN), wishes to allocate `linked.data.gov.au/ship/` for a list of ships that they have published in multiple datasets, `linked.data.gov.au/dataset/ds1/ship/` & `linked.data.gov.au/dataset/ds2/ship/`. The RAN will have to ensure that the allocated register resolves to a collection of ships from both datasets.

Where multiple *Submitting Organization* s wish to combine their data into a single top-level register, they must arrange for federated register presentation, not the AGLDWG.

A multi-class example:

A *Submitting Organization* wishes a top-level register for items of class A and class B. There is some real-world logic making such an allocation sensible so the *Submitting Organization* requests the top-level register `linked.data.gov.au/classAB/` which is approved. A better request though would be for a register of `linked.data.gov.au/classC/` where class C is a superclass of both class A and B.

#### 8.0.1 Use and non-use of Register URI for contained items
A *Submitting Organization* may request a top-level register such as `linked.data.gov.au/classA/` and then present items within that class with URIs such as `linked.data.gov.au/classA/1`, `linked.data.gov.au/classA/2` etc. but may also present items with un-related URIs within the register as long as the class of item (discoverable via de-referenceable RDF) accords with the class(es) for which the register was allocated. The AGLDWG may check the classes of items within a top-level register using automated means.

#### 8.0.2 Subregisters
If a *Submitting Organization* wishes to use a top-level register already allocated for new items in accordance with the class(es) for with the register was allocated, they have two options:

1. arrange with the original *Submitting Organization* to have their items included in the register
2. request a module within the Top-Level Register for their items

Modules requested within a top-level register will be presented as sub-registers of the Top-Level Register. Management of such is the responsibility of the Top-Level Register's manager - the original *Submitting Organisation* who was allocated the URI for it, not the AGLDWG.

### 8.1 Dataset URI pattern
The pattern for allocating Top-Level Register URIs is:

```
register-uri ::=  protocol "://linked.data.gov.au/" register-id "/"
protocol ::= "http" | "https"
register-id ::= *(ALPHA | DIGIT | "-")
```

Where `register-id` is some approximation of the class(es) of object which the register contains. What is a fair approximation and what is not will be judged by the *Controlling Committee*.

An example is that a *Submitter* may request present a register of organisations, containing `Organization`-class individuals as defined in the Organization Ontology [[W3C-2014c]()#ref-W3C-2014c)] and request the allocation of:

`http://linked.data.gov.au/organisation/`

Alternatively, the *Submitter* may request the allocation of:

`http://linked.data.gov.au/org/`

where 'org' is a well-known shortened form of 'organisation'. Either of these requests are suitable for allocation.

Subregisters within a Top-Level Register are to be managed by the manager of the Top-Level register with the `module-id` to be allocated by them. The total URI pattern for this form of modularised register is:

```
modularised-register-uri ::= register-uri "/" module-id
module-id ::= *(ALPHA | DIGIT | "-")
```

### 8.2 Registration Process
This process follows the general process as outlined in Figure 1.

* *Submitter* must be eligible, as per Req 6
  * *Submitter* initiates a requests a PID URI allocation for a dataset URI by creating a complete catalogue record in the AGLDWG LD Resource Catalogue
  * the resource type must be set to 'definitional'
  * request approval status to `submitted`
* *Controlling Committee* is automatically notified to review the requests by the catalogue
* *Controlling Committee* reviews the request and approves it if it passes the metadata and Linked Data tests for a dataset described in [Appendix B](#app-b) and [Appendix A](#app-a), respectively
  * if approved, request approval status to `approved`
  * if not approved, resource status set to `not approved`
  * *Submitter* automatically notified of status change
* if approved, *Steward* implements a URI redirect to the hosted dataset and tests implementation
  * if no collisions with existing patterns are found:
    * if the resource is ready, approval status to `stable`
    * if the resource is not ready, else approval status set to `reserved`
  * if collisions are found, approval status set to `invalid`
  * *Submitter* notified
* *Submitting Organization* is free to use allocated URIs

### 8.3 Required Metadata
Metadata to be supplied for the registration of a Linked Data register, and thus the allocation of a URI for it, must constitute a valid record for such within the AGLDWG LD Resource Catalogue. Record validity is determined using the process outlined in [Appendix B](#app-b).

Entries in the AGLDWG LD Resource Catalogue are public from submission onwards.


## 9. <a id="SecondLevelRegisters"></a>Second-Level Register URIs
At this stage, the AGLDWG recognises there are two sorts of Second-level Registers for which URIs may be allocated:

1. subregisters of a Dataset
2. modularised subregisters of a Top-Level Register

In both cases, the URI arrangements for the Second-Level Register URIs need to be made by the dataset or Top-Level Register manager, however the AGLDWG can assist with implementing redirects for these subregisters within the patterning assigned to a Dataset or Top-Level Register, if requested. Such pattern implementation will follow the workflow given in Figure 3 but will not result in any change to the relevant allocation status of the Dataset or Top-Level Register.

## 10. <a id="References"></a>References
[AGLDWG-2018] <a name="ref-AGLDWG-2018"></a>Australian Government Linked Data Working Group "Governance", web page, 2018. <http://www.linked.data.gov.au/governance>, accessed 2018-07-27.

[AGLDWG-2018b] <a name="ref-AGLDWG-2018b"></a>Australian Government Linked Data Working Group, "Status Vocabulary". SKOS Vocabulary, 22 July 2018. <http://test.linked.data.gov.au/def/status>, accessed 2018-07-22.

[CAB-2010] <a name="ref-CAB-2010"></a>Cabinet Office, "Designing URI Sets for the UK Public Sector", web page, 2010. <https://www.gov.uk/government/publications/designing-uri-sets-for-the-uk-public-sector>, accessed 2018-06-07.  

[CAR-2017] <a href="ref-CAR-2017"></a>Car, Nick; Golodoniuc, Pavel; Klump, Jens. "The challenge of ensuring persistency of identifier systems in the world of ever-changing technology". Data Science Journal. 2017; 16: Article 13. <https://doi.org/10.5334/dsj-2017-013>

##### Not used
[DCMI-2012] <a name="ref-DCMI-2012"></a>Dublin Core Metadata Initiative "DCMI Metadata Terms", web page, 2012. <http://www.dublincore.org/documents/dcmi-terms/>, accessed 2018-06-07.

##### Not used
[IETF-2012] <a name="ref-IETF-2012"></a>Internet Engineering Task Force "RFC6570: URI Template", proposed standard, 2012. <http://tools.ietf.org/html/rfc6570>, accessed 2018-06-07.  

##### Not used
[IETF-1999] <a name="ref-IETF-1999"></a>Internet Engineering Task Force "RFC2616: Hypertext Transfer Protocol -- HTTP/1.1", Request for Comment, 1999. <http://www.ietf.org/rfc/rfc2616>, accessed 2018-06-07.  

[IETF-1997] <a name="ref-IETF-1997"></a>Internet Engineering Task Force, Network Working Group "Key words for use in RFCs to Indicate Requirement Levels", Request for Comments: 2119, 1997. <http://www.ietf.org/rfc/rfc2119>, accessed 2018-06-07.

[IETF-2008] <a name="ref-IETF-2008"></a>Internet Engineering Task Force, Network Working Group "Internet Standard 68: Augmented BNF for Syntax Specifications: ABNF". Internet Engineering Task Force, 2008. <https://tools.ietf.org/html/std68>, accessed 2018-06-07.  

[ISO-2015] <a name="ref-ISO-2015"></a>International Organization for Standardization / International Electrotechnical Commission "ISO/IEC 11179, Information Technology -- Metadata registries (MDR)", standard. <http://metadata-standards.org/11179/>, accessed 2018-06-07.

##### Not used
[FIEL-2005] <a name="ref-FIEL-2005"></a>Fielding, Roy T. "[httpRange-14] Resolved", archived email, 2005. <http://lists.w3.org/Archives/Public/www-tag/2005Jun/0039.html>, accessed 2018-06-07.  

[PC-2017] <a href="ref-PC-2017"></a>Productivity Commission, "Data Availability and Use", public inquiry report, 8 May 2017. <http://www.pc.gov.au/inquiries/completed/data-access>

[REY-2012] <a name="ref-REY-2012"></a>Reynolds, Dave "Registry ontology", Version 0.2. OWL Ontology,  2012-11-11 <http://epimorphics.com/public/vocabulary/Registry.html>, accessed 2018-07-22.

[TBL-2006] <a name="ref-TBL-2006"></a>Berners-Lee, Tim "Linked Data", web page, 2006. <http://www.w3.org/DesignIssues/LinkedData.html>, accessed 2018-06-07.  

[W3C-2008] <a name="ref-W3C-2008"></a>World Wide Web Consortium "Cool URIs for the Semantic Web", W3C Interest Group Note, 03 December 2008. <http://www.w3.org/TR/cooluris/>, accessed 2018-06-07.  

[W3C-2012] <a name="ref-W3C-2012"></a>World Wide Web Consortium "223 Best Practices URI Construction", wiki web page, 2012. <http://www.w3.org/2011/gld/wiki/223_Best_Practices_URI_Construction>, accessed 2018-06-07.

[W3C-2014] <a name="ref-W3C-2014"></a>World Wide Web Consortium "RDF 1.1 Concepts and Abstract Syntax", W3C Proposed Recommendation, 09 January 2014. <http://www.w3.org/TR/rdf11-concepts/>, accessed 2018-06-07.  

[W3C-2014b] <a name="ref-W3C-2014b"></a>World Wide Web Consortium "RDF Schema 1.1", W3C Recommendation, 25 February 2014. <http://www.w3.org/TR/rdf-schema/>, accessed 2018-07-22.

[W3C-2014c] <a name="ref-W3C-2014c"></a>World Wide Web Consortium "The Organization Ontology", W3C Recommendation 16 January 2014. <https://www.w3.org/TR/vocab-org/>, accessed 2018-07-30.

[W3C-2016] <a href="ref-W3C-2016">World Wide Web Consortium, "HashVsSlash", web page, 2016. <https://www.w3.org/wiki/HashVsSlash>, accessed 2018-07-27.

[W3C-2017] <a name="ref-W3C-2017"></a>World Wide Web Consortium "HTML 5.2", W3C Recommendation, 14 December 2017. <https://www.w3.org/TR/html/>, accessed 2018-07-28.

[W3C-2018] <a name="ref-W3C-2018"></a> World Wide Web Consortium, "Linked Data", web page, 2018. <https://www.w3.org/standards/semanticweb/data>, accessed 2018-07-27.

## 11. <a id="app-a"></a>Appendix A: Resource Linked Data requirements
Resources for which the AGLDWG issues PID URIs must be valid Linked Data. Specific requirements for each type of resource are listed below.

#### Definitional resources:
1. ***MUST*** be presented in the Resource Description Framework, RDF [[W3C-2014](#ref-W3C-2014)]
  * the RDF must pass basic RDF syntactic validation
  * the issued PID URI must be able to resolve to at least one standard serialisation of RDF which the AGLDWG takes to be either RDF/XML, Turtle, JSON-LD, N-triples, N-quads or TriG using standard HTTP content negotiation which, for AGLDWG-hosted resources, will be implemented automatically  
  * the RDF must at least indicate a label (`rdfs:label`) for the definitional resource
2. ***SHOULD*** be presented in Hypertext Mark-Up Language version 5, HTML5 [[W3C-2017](#ref-W3C-2017)]
  * the RDF version is considered point-of-truth; the HTML version must faithfully represent the RDF contents
  * the HTML version, if present, will be the default version displayed if no content negotiation directives are used
  * for AGLDWG-hosted resources, the HTML version will be auto-built from supplied RDF using one of several tools: LODE2 for ontologies ([lode2.linked.data.gov.au](http://lode2.linked.data.gov.au)) and the RDA's RVA portal ([vocabs.ands.org.au](http://vocabs.ands.org.au)) for vocabularies.
3. ***MAY*** use either hash or slash URIs for subelements
  * the AGLDWG can host single-file definitional resources which use hash URIs
4. ***MUST*** be valid RDFS documents adhering to the RDF Schema specification [[W3C-2014b](#ref-W3C-2014b)]

The following tests in the Python script file `ldreqs.py` within this repository must pass to ensure definitional resources pass the above criteria:

Requirement | Function name | Purpose
---|---|---
1 | `definitional_required_1` | resolves the access URI of the resource, looks for an HTTP 200 response to a request using an `Accept` header seeking RDF formats, resolves the properly `rdfs:label` for the URI
4 | `definitional_required_4` | resolves RDF from the resource URI and looks within it for valid RDFS constructs

The following tests in the Python script file `ldreqs.py` within this repository will also be run to provide feedback to the *Submitter*:

Requirement | Function name | Purpose
---|---|---
2 | `definitional_optional_2` | resolves the access URI of the resource, looks for an HTTP 200 response to a request using an `Accept` header seeking HTML, confirms the result is valid HTML
3 | `definitional_optional_3` | parses the RDF implementation of the resource and searches for RDFS or OWL classes and determines whether their URIs are hash or slash URIs


#### Datasets:
1. ***MUST*** present a landing page for the dataset in RDF
  * the RDF must pass basic RDF syntactic validation
  * the issued PID URI must be able to resolve to at least one standard serialisation of RDF which the AGLDWG  takes to be either RDF/XML, Turtle, JSON-LD, N-triples or TriG using standard HTTP content negotiation which, for AGLDWG-hosted resources, will be implemented automatically  
  * the RDF must at least indicate a label (`rdfs:label`) for the dataset
2. ***SHOULD*** present a landing page for the dataset in HTML
  * the RDF version is considered point-of-truth; the HTML version must faithfully represent the RDF contents
  * the HTML version, if present, will be the default version displayed if no content negotiation directives are used
  * for AGLDWG-hosted resources, the HTML version may be auto-built from supplied RDF if the dataset is conducive to such building
3. ***MUST*** have all identifiable dataset subelements discoverable via Linked Data
  * all individuals (instances) must be able to be accessed via either hash or slash URIs and those URIs must be discoverable via some RDF mechanism, such as use of a data cube, registry or other ontology that lists them in a way navigable from the dataset URI
  * the data of the individuals may themselves not be in Linked Data formats, for example a subelement of a dataset, identified with a URI that when resolved yields an image
4. ***MAY*** use either hash or slash URIs for subelements
  * the AGLDWG can host single-file definitional resources which use hash URIs

The following tests in the Python script file `ldreqs.py` within this repository must pass to ensure definitional resources pass the above criteria:

Requirement | Function name | Purpose
---|---|---
1 | `dataset_required_1` | resolves the access URI of the resource, looks for an HTTP 200 response to a request using an `Accept` header seeking RDF formats, resolves the properly `rdfs:label` for the URI
3 | `dataset_required_3` | resolves the access URI of the resource, looks for subelements of that resource indicated via `dct:hasPart`, `reg:register` (subitems indicating the dataset as is a `reg:Register`)   

The following tests in the Python script file `ldreqs.py` within this repository will also be run to provide feedback to the *Submitter*:

Requirement | Function name | Purpose  
---|---|---  
2 | `dataset_optional_2` | resolves the access URI of the resource, looks for an HTTP 200 response to a request using an `Accept` header seeking HTML, confirms the result is valid HTML  
4 | `dataset_optional_4` | resolves the access URI of the resource, looks for an HTTP 200 response to a request using an `Accept` header seeking RDF formats, seeks sublements defined using hash or slash URIs stemming form the dataset URI by pattern matching subject triples with the dataset URI  

## 12. <a id="app-b"></a>Appendix B: Resource catalogue item metadata
Resources submitted to the AGLDWG for URI allocation are considered items submitted to a registry and are required to have metadata supplied according to the Registry Ontology [[REY-2012](#ref-REY-2012)]. This enables resource management, cataloguing and delivery of registry information as Linked Data. Entries in the PID Allocations Catalogue ([catalogue.linked.data.gov.au](http://catalogue.linked.data.gov.au)), which are required for PID URI allocation, can only be saved when valid metadata is entered. Entry metadata is also changed as the PID request that the record represents passes through an approval workflow. The catalogue uses simple labels in its forms to indicate elements and a mapping for each label and the equivalent formal predicates in Registry Ontology, and their required cardinality, are given in Table 2.

**Table 2**: PID Allocations Catalogue for elements for catalogue items, their Registry Ontology equivalents, cardinalities and notes. The Registry Ontology element prefixes are:

Catalogue Element | Registry Ontology Element |  Cardinality | Notes  
---|---|---|---
Title | `rdfs:label` | 1 | \-  
Description | `dct:description` | 1 | \-  
\- | `dct:dateSubmitted` | 1 | automatically filled on catalogue item creation  
Date Accepted | `dct:dateAccepted` | 0 or 1 | 0 when created, 1 when accepted  
Date Modified | `dct:modified` | 1 | automatically filled by catalogue  
Item Type | `reg:itemClass` | 1 | one of 'dataset', 'definitional' or 'register'  
Submitter | `reg:submitter` | 1 | one of the approved *Submitting Organisations*  
Acceptance Status | `reg:status` | 1 | one of the Registry Ontology's status vocab terms  
