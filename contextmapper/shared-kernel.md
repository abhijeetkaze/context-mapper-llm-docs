
# Shared Kernel

The Shared Kernel pattern describes a relationship between two bounded contexts and is used on a [context map](/docs/context-map/) in CML. The [Language Semantics](https://contextmapper.org/docs/language-model/) page describes all relationship types that are supported in CML.

## Syntax

Note that currently two different syntax variants exist. The following code snippets illustrate both variants:

```
CargoBookingContext [SK]<->[SK] VoyagePlanningContext {
  implementationTechnology = "Java Library"
}

```

Note that with this syntax (with the arrows *<->*) it does not matter which bounded context is on which side, since this is a symmetric relationship. If you switch the bounded contexts, it has the same meaning semantically.

```
CargoBookingContext Shared-Kernel VoyagePlanningContext {
  implementationTechnology = "Java Library"
}

```

### Default Symmetric Relationship

**Note** that the Shared Kernel is the default symmetric relationship. Omitting the concrete relationship type within the brackets as follows, declares a
Shared Kernel relationship too. However, with this syntax a reader has to know this behavior and cannot explicitly see that it is **not** a Partnership
relationship:

```
CargoBookingContext <-> VoyagePlanningContext

```

### Implementation Technology

With the *implementationTechnology* keyword you can specify how the relationship is implemented.

### Relationship Name

With a colon it is possible (optionally) to add a relationship name to the specification, as illustrated within this example:

```
CargoBookingContext Shared-Kernel VoyagePlanningContext : BookingVoyageRelationship {
  implementationTechnology = "Java Library"
}

```

[Improve this page](https://github.com/ContextMapper/contextmapper.github.io/blob/master/_docs/language-reference/shared-kernel.md)

---

* [← Previous](/docs/partnership/)
* [Next →](/docs/customer-supplier/)

