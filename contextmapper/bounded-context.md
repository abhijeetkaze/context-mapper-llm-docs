
# Bounded Context

Bounded Context a key concept in strategic DDD. The interpretation and usage of the pattern in Context Mapper is explained in the article [“Domain-driven Architecture Modeling and Rapid Prototyping with Context Mapper”](https://contextmapper.org/media/978-3-030-67445-8_11_AuthorsCopy.pdf).

Bounded Contexts are defined on the root level of a CML (\*.cml) file and then referenced on a context map which defines the relationships with other bounded contexts. Have a look at [context map](/docs/context-map/) to see how you add a bounded context to your context map.

## Syntax

The following example illustrates how a bounded context is defined in CML (syntactical features). The **Customer Management** context is a context within our fictitious insurance company example. The whole example with the context map and all bounded contexts can be found [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example).

```
BoundedContext CustomerManagementContext implements CustomerManagementDomain {
  type = FEATURE
  domainVisionStatement = "The customer management context is responsible for ..."
  implementationTechnology = "Java, JEE Application"
  responsibilities = "Customers", "Addresses"
  knowledgeLevel = CONCRETE

  Module addresses {
    Aggregate Addresses {
      Entity Address {
        String city
      }
    }
  }
  Aggregate Customers {
    Entity Customer {
      aggregateRoot

      - SocialInsuranceNumber sin
      String firstname
      String lastname
      - List<Address> addresses
    }
  }
}

```

**Note:** Bounded Context names must be unique within your CML model.

The **implements** keyword specifies which domain or subdomains are implemented by this bounded context. Behind the **implements**
keyword you can either reference a list of subdomains (comma-separated) or one top-level domain. Consult [Subdomain](/docs/subdomain/) to learn how subdomains are specified.

Attribute values are assigned as follows:

```
BoundedContext ContextMapperTool refines StrategicDomainDrivenDesignContext {
  type FEATURE
  domainVisionStatement "Context Mapper provides a formal way to model strategic DDD Context Maps."
  implementationTechnology "Java, Eclipse"
}

```

An equal sign (=) to assign attribute values may be present but can be omitted.

The example above also shows how you can let one bounded context refine another one (with the **refines** keyword). This feature allows you to create some kind of an inheritance hierarchy in case one bounded context can be seen as a refinement of another bounded context. However, note that this is only a modeling information and generators do not recursively resolve the domain model (Aggregates, etc.) of refined bounded contexts.

All of the following attributes are **optional** and you do not have to specify them all.

### Bounded Context Type

With the *type* keyword you define the bounded contexts type, which can be one of the following:

* FEATURE
* APPLICATION
* SYSTEM
* TEAM

The type provides an indicator for which reason a bounded context may have been evolved. It further allows you to specify from which
viewpoint you describe your bounded contexts. FEATURE contexts are analysis or early design abstractions, taking a functional scenario view. Application contexts represent more
elaborated, logical designs and implementation views; system contexts add a more physical, process- and deployment-oriented view.

Finally, you may want to create a team map, within which every bounded context reflects a team, inspired by [Brandolini](https://www.infoq.com/articles/ddd-contextmapping). A team map further allows you to specify which team is implementing which bounded contexts (of type FEATURE, APPLICATION, or SYSTEM). Note that the context map type must be ORGANIZATIONAL to specify a team map. The corresponding syntax is described under [context map](/docs/context-map) and an example for a team map can be found
[here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example).

The following table lists examples for each Bounded Context type to illustrate how we interpret them:

| Context Type | Examples |
| --- | --- |
| FEATURE | Such a Bounded Context represents a boundary around a set of functional features (user stories / use cases). For example, everything that is related to *customer* management in an insurance scenario: create customer, update customer, update customer address, etc. |
| APPLICATION | A Bounded Context of this type represents an application from a logical viewpoint. For example, a software solution for an insurance company (an example can be found [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example)) consists of multiple applications: a self-service frontend application for the customers, a backend system to manage the customers and contract, etc. An application typically encompasses multiple functional features. In a (micro-)service-oriented architecture, each (micro-)service can be seen as an application. |
| SYSTEM | The system Bounded Context allow to model a software from a more physical perspective (deployment). Examples for systems: a single page application for the frontend, a Spring Boot application that realizes the domain logic, an Oracle database that holds the data, etc. Thus, an application typically consists of multiple systems. |
| TEAM | A development team can also represent a Bounded Context. For example in our [insurance example](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example#team-map), multiple teams work on different parts of the software: *customer frontend* team, customer backend\_ team, *contracts* team, etc. |

You can evolve the different types of Bounded Context with our [Rapid Object-oriented Analysis and Design](/docs/rapid-ooad/) CML transformations. From functional requirements
written as user stories or use cases you can derive Bounded Contexts of the type FEATURE and/or APPLICATON. From those features you can then derive Bounded Contexts of the
type SYSTEM automatically. You can find more about this automated transformations [here](/docs/rapid-ooad/).

### Domain Vision Statement

With the *domainVisionStatement* keyword you can describe the vision statement of your bounded context, according to the DDD Domain Vision Statement pattern. See [this page](/docs/domain-vision-statement/).

### Implementation Technology

The *implementationTechnology* attribute allows you to add information about how the corresponding bounded context is implemented. Note that this attribute does not correspond to any DDD pattern.

### Responsibility Layers

With the *responsibilities* keyword you are allowed to specify the responsibilities of the bounded context, according to the DDD Responsibility Layers pattern. See [responsibility layers](/docs/responsibility-layers/).

### Knowledge Level

With the *knowledgeLevel* attribute you define the knowledge level of the bounded context which can be one of the following two:

* CONCRETE
* META

This attribute allows you to define the knowledge level according to the DDD Knowledge Level pattern. See [this page](/docs/knowledge-level/).

### Support for Bounded Context Canvases

To support Bounded Context Canvases, use these optional fields in `BoundedContext`:

* `businessModel`. Free text; common values include:
  + UNDEFINED
  + REVENUE
  + ENGAGEMENT
  + COMPLIANCE
  + COST\_REDUCTION
* `evolution`. One of:
  + UNDEFINED
  + GENESIS
  + CUSTOM\_BUILT
  + PRODUCT
  + COMMODITY

Further reading on bounded context canvases:

* [*The Bounded Context Canvas*](https://github.com/ddd-crew/bounded-context-canvas)
* [*Bounded Context Canvas V3: Simplifications and Additions*](https://medium.com/nick-tune-tech-strategy-blog/bounded-context-canvas-v2-simplifications-and-additions-229ed35f825f)
* [*DDD re-distilled*](https://yoan-thirion.gitbook.io/knowledge-base/software-architecture/ddd-re-distilled)
* [*What I talk about when I talk about Domain-Driven Design by Andrew Harmel-Law*](https://youtu.be/6nrRfCkeAKU)

### Team *realizes* Bounded Context

If your bounded context is of the type TEAM, you can specify which bounded context the team implements by using the *realizes* keyword. The following example illustrates this:

```
BoundedContext CustomersBackofficeTeam implements CustomerManagementDomain realizes CustomerManagementContext {
  type = TEAM
  domainVisionStatement = "This team is responsible for implementing ..."
}

```

## The Bounded Context Building Blocks

Within a bounded context, you can create *Modules* and *Aggregates* as illustrated in the example at the beginning of this page. On this tactical DDD level we integrated the [Sculptor DSL](https://sculptor.github.io/).
This means within a module and an aggregate you can use all the [Sculptor features](https://sculptor.github.io/documentation/advanced-tutorial) to specify your bounded context, such as Entities, Value Objects, Domain Events, Services, Repositories, etc.

Use the [Sculptor Documentation](https://sculptor.github.io/documentation/advanced-tutorial) and our [examples](https://github.com/ContextMapper/context-mapper-examples) to find out how you specify your bounded context.
Note that the Aggregate pattern is the only tactical DDD pattern where we changed the Sculptor syntax and adapted it to our interpretation and requirements. See [Aggregate](/docs/aggregate/).

## Semantic Rules

Note that semantic rules (validators) exist for bounded contexts within CML. This means that not every combination of patterns and concepts is allowed, even if it would be syntactically correct.
The following rules apply to a bounded context:

* The *realizes* keyword of the bounded context rule can only be used if the type of the bounded context is TEAM.

For a summary of all semantic rules and justifications, please consult [Language Semantics](/docs/language-model/).

[Improve this page](https://github.com/ContextMapper/contextmapper.github.io/blob/master/_docs/language-reference/bounded-context.md)

---

* [← Previous](/docs/context-map/)
* [Next →](/docs/subdomain/)

