
# Context Map

The context map is the most important element of CML, implementing the DDD Context Map pattern.
A context map contains bounded contexts and defines their relationships. The interpretation and usage of the pattern in Context Mapper is explained in the article [“Domain-driven Architecture Modeling and Rapid Prototyping with Context Mapper”](https://contextmapper.org/media/978-3-030-67445-8_11_AuthorsCopy.pdf).

## Syntax

The following CML code snippet illustrates an example for a context map, according to our customized [DDD Sample](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/ddd-sample).
With the *contains* keyword you add a bounded context to the map.

```
ContextMap {
  type = SYSTEM_LANDSCAPE
  state = AS_IS

  contains CargoBookingContext
  contains VoyagePlanningContext
  contains LocationContext

  CargoBookingContext [SK]<->[SK] VoyagePlanningContext
}

```

Alternatively, you can use only one *contains* keyword and list all bounded contexts comma-separated:

```
ContextMap DDDSampleContextMap {
  type SYSTEM_LANDSCAPE
  state AS_IS

  contains CargoBookingContext, VoyagePlanningContext, LocationContext

  CargoBookingContext [SK]<->[SK] VoyagePlanningContext
}

```

As you can see in the example above, it is also possible to name a context map (the name is optional). The equal sign (=) to assign an attribute value as done in the first example can be omitted as well.

A context map can be of one of the following **types**:

* SYSTEM\_LANDSCAPE
* ORGANIZATIONAL

A SYSTEM\_LANDSCAPE represents the default type of context map in which the bounded contexts represent software systems (or applications). The second type, an ORGANIZATIONAL map (or ‘team map’), illustrates the relationships between teams. An example for such a team map can be found [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/insurance-example).

The **state** attribute accepts the following two values, expressing whether the given context map represents the current or a desired state (this distinction is often made in [enterprise architecture management](https://searcherp.techtarget.com/definition/enterprise-asset-management-EAM) and [portfolio- or program-level project planning](https://www.pmi.org/learning/library/integrated-portfolio-program-management-7409)):

* AS\_IS
* TO\_BE

## Relationships

According to our [semantic model](/docs/language-model/), we support the following symmetric relationships:

* Partnership (P)
* Shared Kernel (SK)

The asymmetric relationships are represented by the following two types:

* Upstream-Downstream (generic)
* Customer-Supplier (C/S), a special form of an Upstream-Downstream relationship

**Note:** A customer-supplier relationship is an upstream-downstream relationship where the downstream priorities factor
into upstream planning. The upstream team may succeed interdependently of the fate of the downstream team and therefore the needs of
the downstream have to be addressed by the upstream. They interact as **customer** and **supplier**.
A generic upstream-downstream relationship is not necessarily a customer-supplier relationship! (in CML you have to express this
explicitly)

The syntax for upstream-downstream relationships is explained below. To learn about the syntax of customer-supplier relationships, please visit [Customer/Supplier](/docs/customer-supplier/).

The symmetric relationships and their syntax are introduced on separate pages: [Partnership](/docs/partnership/) and [Shared Kernel](/docs/shared-kernel/).

Upstream-Downstream relationships can be defined with three different syntax variants, all illustrated with the examples below:

```
CargoBookingContext [D]<-[U] LocationContext

```

```
LocationContext [U]->[D] CargoBookingContext

```

```
LocationContext Upstream-Downstream CargoBookingContext

```

```
CargoBookingContext Downstream-Upstream LocationContext

```

All of the four variants are semantically equivalent. Note that the arrow *->* always points from the upstream to the downstream and thus expresses an *influence flow*
(the upstream has an influence on the downstream, but the downstream has no influence on the upstream).

A colon at the end assigns a relationship a name:

```
CargoBookingContext [D]<-[U] LocationContext : CargoLocationRelationship

```

**Note:** The following quick upstream/downstream syntax without brackets can be used as well. It denotes a common upstream/downstream relationship without any roles. However, with this syntax it is less clear for a reader that you declare an upstream/downstream and *not* a customer/supplier relationship.

```
CargoBookingContext <- LocationContext

```

```
LocationContext -> CargoBookingContext

```

### Relationship Roles

You can further specify the relationship roles such as Open Host Service (OHS) or Anti-Corruption Layer (ACL) within the brackets.
Roles must always be specified behind the **U** (upstream) and the **D** (downstream) if they are not omitted.

```
VoyagePlanningContext [D,ACL]<-[U,OHS,PL] LocationContext

```

Since the arrow already indicates which Bounded Context is upstream and which is downstream, it is also possible to add the relationship roles within the brackets without the **U** and the **D**:

```
VoyagePlanningContext [ACL]<-[OHS,PL] LocationContext

```

If you use the *Upstream-Downstream* or *Downstream-Upstream* keywords the roles are declared equivalently, but without the **D** and **U** (note that it does not matter if you write a whitespace before or after the brackets, or both):

```
VoyagePlanningContext[ACL] Downstream-Upstream [OHS,PL]LocationContext

```

Upstream roles are defined by the [Open Host Service (OHS)](/docs/open-host-service/) and
[Published Language (PL)](/docs/published-language/) patterns. Downstream roles are [Conformist (CF)](/docs/conformist/) and
[Anticorruption Layer (ACL)](/docs/anticorruption-layer/).

### Relationship Attributes

By using brackets {}, you can specify additional attributes for a relationship:

* implementationTechnology
* downstreamRights
* exposedAggregates

#### Implementation Technology

Within the body of the declaration, it is possible to specify the implementation technology used to realize this relationship:

```
VoyagePlanningContext [D,ACL]<-[U,OHS,PL] LocationContext {
    implementationTechnology = "RESTful HTTP"
}

```

#### Downstream Governance Rights

The attribute *downstreamRights* defines which governance rights, and therefore which influence, the downstream has on the upstream within the specified relationship:

```
VoyagePlanningContext [D,ACL]<-[U,OHS,PL] LocationContext {
    implementationTechnology = "RESTful HTTP"
    downstreamRights = VETO_RIGHT
}

```

The possible governance rights values are:

* INFLUENCER
* OPINION\_LEADER
* VETO\_RIGHT
* DECISION\_MAKER
* MONOPOLIST

#### Exposed Aggregates

The *exposedAggregates* attribute offers the possibility to declare which [Aggregates](/docs/aggregate) of the **upstream** bounded context are exposed in order to realize this relationship. The attribute takes a comma-separated list of references to Aggregates. The referenced Aggregates must be part of the upstream context of the relationship.

```
VoyagePlanningContext [D,ACL]<-[U,OHS,PL] LocationContext {
    implementationTechnology = "RESTful HTTP"
    downstreamRights = VETO_RIGHT
    exposedAggregates = Customers, Addresses
}

```

### Special Case: Customer/Supplier

For the Customer-Supplier relationship, which is a special form of Upstream-Downstream relationship, please visit [Customer-Supplier](/docs/customer-supplier).

## Semantic Rules

Note that semantic rules (validators) exist for context maps within CML. This means that not every combination of patterns and concepts is allowed (even if it was syntactically correct).
The following rules apply to a context map:

* A Bounded Context which is not part of the Context Map (referenced with the *contains* keyword), can not be referenced from a relationship rule within that Context Map.
* A Bounded Context of the type TEAM can not be contained in a Context Map of type SYSTEM\_LANDSCAPE.
* If the type of a Context Map is ORGANIZATIONAL, every Bounded Context added to it (indicated by the keyword *contains*) has to be of the type TEAM.

For a summary of all semantic rules and further justifications, please consult [Language Semantics](/docs/language-model/).

[Improve this page](https://github.com/ContextMapper/contextmapper.github.io/blob/master/_docs/language-reference/context-map.md)

---

* [← Previous](/docs/language-model/)
* [Next →](/docs/bounded-context/)

