
# Generic Generator (Templating)

* [Introduction](#introduction)
* [Data Model](#data-model)
* [Helper Functions](#helper-functions)
* [User Guide](#user-guide)
* [Example Templates](#example-templates)

## Introduction

The generic generator is based on [Freemarker](https://freemarker.apache.org/) templates. It allows Context Mapper users to generate arbitrary text files from CML Context Maps. One can generate for example Markdown, JSON, XML, or any other textual output formats by providing a corresponding [Freemarker](https://freemarker.apache.org/) template (*\*.ftl* file).

### Simple Example

This simple example illustrates how the generator works. The following Freemarker template outputs the names of all Bounded Contexts on the Context Map:

```
The Context Map '${contextMap.name}' contains the following Bounded Contexts:

<#list contextMap.boundedContexts as bc>
${bc.name}
</#list>

```

Applied to our [insurance example](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example) the generator produces
the following output:

```
The Context Map 'InsuranceContextMap' contains the following Bounded Contexts:

CustomerManagementContext
CustomerSelfServiceContext
PrintingContext
PolicyManagementContext
RiskManagementContext
DebtCollection

```

## Data Model

In order to write your own Freemarker templates, you have to know the data model exposed by Context Mapper. In the following we provide an overview over this CML model.

**Note:** We do not document the tactic DDD parts within Bounded Contexts in all details. In case your template needs information on that level please use
our [JavaDoc](https://www.javadoc.io/doc/org.contextmapper/context-mapper-dsl/latest/org/contextmapper/dsl/contextMappingDSL/package-summary.html) documentation
to obtain the necessary information about the data model.

**Note:** The variable names of the model documented below must be used case-sensitively in Freemarker templates.

### Root Level

The root level of the model contains the following elements:

```
(root)
  |
  +- contextMap                    Context Map object
  |
  +- boundedContexts               Bounded Context list
  |
  +- domains                       Domains list
  |
  +- imports                       Imports list
  |
  +- useCases                      Use cases list
  |
  +- timeStamp                     Time stamp with current/generation time
  |
  +- fileName                      name of CML file
  |
  +- projectName                   name of Eclipse project
  |
  +- contextMapperVersion          version of the Context Mapper plugin and the CML language
  |
  +- userName                      name of the current system user

```

The corresponding CML objects and their syntax can be found in our language reference: [Context Map](/docs/context-map/), [Bounded Context](/docs/bounded-context/), [Domains and Subdomains](/docs/subdomain/), [imports](/docs/imports/), [use cases](/docs/aggregate/#use-case-declaration).

### Context Map

The *contextMap* root element of the model contains the following data (the values in double quotes `"..."`are just examples):

```
contextMap
  |
  +- name = "ExampleContextMap"
  |
  +- type = "SYSTEM_LANDSCAPE"
  |
  +- state = "TO_BE"
  |
  +- boundedContexts               List of Bounded Contexts that are added to the Context Map
  |
  +- relationships                 List of Context Map relationships

```

#### Relationships

If you use relationships, you must respect the different types as illustrated in our language [meta model](/docs/language-model/). The following types of relationships exist:

* *SymmetricRelationship*
  + *Partnership*
  + *SharedKernel*
* *UpstreamDownstreamRelationship*
  + *CustomerSupplierRelationship*

Depending on the relationship type (symmetric or upstream-downstream), the objects have a different structure.

The structure of a **SymmetricRelationship** is as follows:

```
relationship
  |
  +- name = "ExampleRelationship"  Optional relationship name (nullable)
  |
  +- implementationTechnology = "Java Library"
  |
  +- participant1                  Bounded Context object (first relationship participant)
  |
  +- participant2                  Bounded Context object (second relationship participant)

```

The structure of an **UpstreamDownstreamRelationship** on the other hand is as follows:

```
relationship
  |
  +- name = "ExampleRelationship"  Optional relationship name (nullable)
  |
  +- implementationTechnology = "RESTful HTTP"
  |
  +- upstream                      Bounded Context object (upstream context)
  |
  +- downstream                    Bounded Context object (downstream context)
  |
  +- upstreamRoles                 List of upstream roles (OHS, PL)
  |   |
  |   +- (1st)
  |   |   |
  |   |   +- name = "OHS"
  |   |
  |   +- (2nd)
  |       |
  |       +- name = "PL"
  |
  +- downstreamRoles               List of downstream roles (ACL, CF)
  |   |
  |   +- (1st, 2nd)
  |       |
  |       +- name = "ACL"          Semantics only allows one role here (ACL or CF)
  |
  +- upstreamExposedAggregates     List of Aggregate objects
  |
  +- downstreamGovernanceRights
      |
      +- name = "INFLUENCER"

```

#### Relationship Type Checking

To respect the different structures when processing the relationship list, we provide a method that allows you to check the type of the relationship:

```
<#if instanceOf(relationship, SymmetricRelationship)>
...
</#if>

```

```
<#if instanceOf(relationship, UpstreamDownstreamRelationship)>
...
</#if>

```

You can also check the type of concrete relationship:

```
<#if instanceOf(relationship, Partnership)>
...
</#if>

```

```
<#if instanceOf(relationship, CustomerSupplierRelationship)>
...
</#if>

```

### Bounded Context

The *boundedContexts* root element of the model contains a list of *BoundedContext* objects. The *BoundedContext* object has the following structure:

```
boundedContext
  |
  +- name = "CustomerManagement"
  |
  +- implementedDomainParts        List of implemented domain parts
  |   |
  |   +- (1st)                     (example: first element is a _Domain_)
  |   |   |
  |   |   +- name = "Insurance"
  |   |   |
  |   |   +- domainVisionStatement = "Insurance application vision statement ..."
  |   |   |
  |   |   +- subdomains            List of subdomains
  |   |
  |   +- (2nd)                     (example: second element is a _Subdomain_)
  |       |
  |       +- name = "CustomerManagement"
  |       |
  |       +- domainVisionStatement = "Customer management vision statement ..."
  |       |
  |       +- type
  |       |   |
  |       |   +- name = "CORE_DOMAIN"
  |       |
  |       +- entities              List of Entity objects
  |
  +- realizedBoundedContexts       List of Bounded Context objects
  |
  +- refinedBoundedContext         Bounded Context object
  |
  +- domainVisionStatement = "This Bounded Contexts goal is ..."
  |
  +- type
  |   |
  |   +- name = "FEATURE"
  |
  +- responsibilities              List of responsibilities (strings)
  |   |
  |   +- (1st)
  |   |   |
  |   |   +- "Managing customers"
  |   |
  |   +- (2nd)
  |       |
  |       +- "Managing addresses"
  |
  +- implementationTechnology = "Spring Boot"
  |
  +- knowledgeLevel
  |   |
  |   +- name = "META"
  |
  +- modules                       List of module objects (Sculptor)
  |   |
  |   +- (1st)
  |       |
  |       +- name = "ExampleModule"
  |       |
  |       +- aggregates            List of Aggregate objects
  |
  +- aggregates                    List of Aggregate objects

```

**Note:** The attribute *implementedDomainParts* of the *BoundedContext* returns a list of *DomainParts*. A *DomainPart* can either be a *Domain* or a *Subdomain*. Both have a *name* and a *domainVisionStatement*. As long as you only use these two attributes you don’t have to check for the type. However, if you want to access the *type* attribute of a *Subdomain* you have to check if the *DomainPart* is a *Subdomain* first:

```
<#if instanceOf(domainPart, Subdomain)>
...
</#if>

```

### Aggregate

Bounded Contexts contain a set of Aggregates that have the following structure (rough sketch, the JavaDoc has the details):

```
aggregate
  |
  +- name = "Customers"
  |
  +- responsibilities              List of responsibilities (strings)
  |   |
  |   +- (1st)
  |       |
  |       +- "Managing customers"
  |
  +- useCases                      List of use case objects
  |
  +- owner                         Bounded Context object
  |
  +- knowledgeLevel
  |   |
  |   +- name = "META"
  |
  +- likelihoodForChange
  |   |
  |   +- name = "NORMAL"
  |
  +- services                      List of Service objects (Sculptor)
  |
  +- resources                     List of Resource objects (Sculptor)
  |
  +- consumers                     List of Consumer objects (Sculptor)
  |
  +- domainObjects                 List of SimpleDomainObject objects (Sculptor)

```

We do not document the structures below Aggregates (Sculptor) here. Please consult the
[JavaDoc](https://www.javadoc.io/doc/org.contextmapper/context-mapper-dsl/latest/org/contextmapper/dsl/contextMappingDSL/Aggregate.html) documentation of the Aggregate.

**Note**: The *domainObjects* list contains all domain objects such as Entities, Value Objects, etc. Sculptor defines the following overall type hierarchy:

* SimpleDomainObject
  + BasicType
  + DataTransferObject
  + DomainObject
    - Entity
    - Event
      * CommandEvent
      * DomainEvent
    - ValueObject
  + Enum
  + Trait

To respect the different structures of these types, you again can use our *instanceOf* method:

```
<#if instanceOf(domainObject, Entity)>
...
</#if>

```

As already mentioned, you find the structure of all these domain objects in our
[JavaDoc](https://www.javadoc.io/doc/org.contextmapper/context-mapper-dsl/latest/org/contextmapper/dsl/contextMappingDSL/Aggregate.html) documentation.

### Domains

The *domains* root element of the model contains a list of *DomainPart* objects which can either be *Domains* or *Subdomains*. Use our *instanceOf* method to check of which type a *DomainPart* is:

```
<#if instanceOf(domainPart, Subdomain)>
...
</#if>

```

The structure of a *Domain* object is the following:

```
domain
  |
  +- name = "Insurance"
  |
  +- domainVisionStatement = "Insurance domain vision statement ..."
  |
  +- subdomains                    List of Subdomain objects

```

The structure of a *Subdomain* object is as follows:

```
subdomain
  |
  +- name = "Insurance"
  |
  +- domainVisionStatement = "Insurance domain vision statement ..."
  |
  +- type
  |   |
  |   +- name = "CORE_DOMAIN"
  |
  +- entities                      List of Entity objects

```

### Imports

CML models can import other files via imports. The mechanism is explained [here](/docs/imports/). Imports can be accessed on the root level of the model (*imports*) and have the following structure:

```
import
  |
  +- importURI = "./other-file.cml"

```

### Use Cases

The *useCases* root element of the model contains a list of *UseCase* objects which have the following structure:

```
usecase
  |
  +- name = "UpdateCustomer"
  |
  +- isLatencyCritical = false
  |
  +- nanoentitiesRead              List of nanoentities that are read by this use case (strings)
  |   |
  |   +- (1st)
  |   |   |
  |   |   +- "Customer.firstName"
  |   |
  |   +- (2nd)
  |       |
  |       +- "Customer.lastName"
  |
  +- nanoentitiesWritten           List of nanoentities that are written by this use case (strings)
      |
      +- (1st)
      |   |
      |   +- "Customer.firstName"
      |
      +- (2nd)
          |
          +- "Customer.lastName"

```

### Additional Root Attributes

The following additional attributes are currently available on the root level of the model:

* *timestamp:* generation time stamp (for example *26.02.2020 17:20:40 CET*)
* *filename:* name of the CML file (for example *ExampleModel.cml*)
* *projectName:* name of the Eclipse project that contains the CML file
* *contextMapperVersion:* the current version of Context Mapper that was used to generate the output (for example *v5.9.4*)
* *userName:* the name of the user that generated the output (OS username)

## Helper Functions

The following functions can be used in the Freemarker templates to help processing the model described above:

### Bounded Context Filtering

The functions *filterStructuralBoundedContexts* and *filterTeams* can be used to filter teams and Bounded Contexts which are not teams respectively. The following example lists all Bounded Contexts that are not teams:

```
<#list filterStructuralBoundedContexts(boundedContexts) as bc>
  Bounded Context: ${bc.name}
</#list>

```

This example on the other hand lists all teams:

```
<#list filterTeams(boundedContexts) as bc>
  Bounded Context: ${bc.name}
</#list>

```

### Type Checking

The meta-model behind CML contains a few inheritance hierarchies which make it unavoidable that you sometimes have to check of which type an object is. Examples with relationships and domains vs. subdomains have already been shown above. The function *instanceOf* allows to check which type of relationship or subdomain an object has:

```
<#if instanceOf(relationship, UpstreamDownstreamRelationship)>
...
</#if>

```

```
<#if instanceOf(domainPart, Subdomain)>
...
</#if>

```

### Get Type String of *ComplexType*

If you work on the tactic DDD level with attributes and methods (parameters and return types) you may want to render the type of an attribute, parameter, or return type.
This part of the DSL is based on [Sculptor](https://sculptor.github.io/), and the types are typically instances of the
[ComplexType](https://www.javadoc.io/doc/org.contextmapper/context-mapper-dsl/latest/org/contextmapper/tactic/dsl/tacticdsl/ComplexType.html) object. Depending on if it is primitive type or a reference to another type, rendering the type as a string is quite cumbersome. The function *getType* which takes a
[ComplexType](https://www.javadoc.io/doc/org.contextmapper/context-mapper-dsl/latest/org/contextmapper/tactic/dsl/tacticdsl/ComplexType.html) as a parameter returns a simple string representing the type:

```
<#list simpleDomainObject.operations as operation>
  operation ${operation.name} returns type ${getType(operation.returnType)}
</#list>

```

## User Guide

To use our generic, [Freemarker](https://freemarker.apache.org/) template-based generator, you need two files within your workspace:

* The input CML model (\*.cml)
* The [Freemarker](https://freemarker.apache.org/) template (\*.ftl)

The generator can be called from the context menus of the CML editors in VS Code or Eclipse. A documentation how to call the generators can also be found [here](/docs/generators/#using-the-generators).

**Note:** All generator outputs will be generated into the *src-gen* folder.

Eclipse as well as VS Code will ask you to choose a \*.ftl file from your filesystem and to define the output file name (which will then be generated into *src-gen*).

### Freemarker Version

Context Mapper uses [Freemarker](https://freemarker.apache.org/), currently Version 2.3.30.

## Example Templates

### Eclipse

The Context Mapper Eclipse plugin comes with sample Freemarker templates. Use the *Freemarker Generator Template Examples* wizard via *File -> New -> Example…* to create the sample project containing the Freemarker templates:

[![Create Sample Project with Freemarker Templates (1)](/img/screenshot-new-freemarker-example-project-1.png)](/img/screenshot-new-freemarker-example-project-1.png)

[![Create Sample Project with Freemarker Templates (2)](/img/screenshot-new-freemarker-example-project-2.png)](/img/screenshot-new-freemarker-example-project-2.png)

### Visual Studio Code

In VS Code we do not deliver the example templates with the extension itself. However, you can just download the \*.ftl files from [here](https://github.com/ContextMapper/context-mapper-dsl/tree/master/org.contextmapper.dsl.ui/samples/freemarker) and use it with our generator in VS Code.

### Provided Examples

The project currently contains the following example templates:

* Ubiquitous language glossary written in Markdown (currently a full report)
  + Currently a full report of the model. A future version of the template will generate a glossary only.
* [JHipster Domain Language (JDL)](https://www.jhipster.tech/jdl/) template to [generate Microservices from CML models](/docs/jhipster-microservice-generation/)
* CSV files to export stakeholder and value register data (as part of the [VDAD support](/docs/vdad-support/))

[Improve this page](https://github.com/ContextMapper/contextmapper.github.io/blob/master/_docs/generators/generic-freemarker-generator.md)

---

* [← Previous](/docs/service-cutter/)
* [Next →](/docs/event-storming/)

