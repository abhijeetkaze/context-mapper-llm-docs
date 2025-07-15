
# Customer/Supplier

The Customer/Supplier pattern describes a relationship between two bounded contexts and is used on a [context map](/docs/context-map/) in CML.

**Note** that according to our understanding of the patterns and our [semantic model](/docs/language-model/)
the customer-supplier relationship is a special case of a upstream-downstream relationship. With the **Customer-Supplier**
keyword you always declare customer-supplier relationships. For 'generic' upstream-downstream relationships which are not
customer-supplier relationships, use the **Upstream-Downstream** keyword explained at [context map](/docs/context-map/).

A customer-supplier relationship is an upstream-downstream relationship where the downstream priorities factor
into upstream planning. The upstream team may succeed interdependently of the fate of the downstream team and therefore the needs of
the downstream have to be addressed by the upstream. They interact as **customer** and **supplier**.
A generic upstream-downstream relationship is not necessarily a customer-supplier relationship! (in CML you have to express this
explicitly)

## Syntax

Customer-Supplier relationships can be defined with three different syntax variants, all illustrated with the examples below:

```
CustomerSelfServiceContext [D,C]<-[U,S] CustomerManagementContext

```

```
CustomerManagementContext [U,S]->[D,C] CustomerSelfServiceContext

```

```
CustomerSelfServiceContext Customer-Supplier CustomerManagementContext

```

```
CustomerManagementContext Supplier-Customer CustomerSelfServiceContext

```

All of the four variants are semantically equivalent. Note that the arrow *->* always points from the supplier (upstream) to the customer (downstream)
and thus, expresses the influence flow (the supplier has an influence on the customer, but the customer has no influence on the supplier).

In a Customer/Supplier relationship definition you can also omit the **U** (upstream) and **D** (downstream) specification, since the supplier is always the
upstream and the customer always the downstream:

```
CustomerSelfServiceContext [C]<-[S] CustomerManagementContext

```

With a colon at the end, you can give every relationship a name:

```
CustomerSelfServiceContext [D,C,ACL]<-[U,S,PL] CustomerManagementContext : Customer_Frontend_Backend_Relationship { // Relationship name is optional
  implementationTechnology = "RESTful HTTP"
}

```

Within the brackets you can further specify the relationship roles such as Open Host Service (OHS) or Anti-Corruption Layer (ACL).
Roles must always be specified behind the **U**/**S** (upstream/supplier) and the **D**/**C** (downstream/customer) signs, as shown in the example above.
Within the body of the declaration it is possible to specify the implementation technology.

If you use the *Customer-Supplier* or *Supplier-Customer* keyword instead of the arrows, the roles are declared equivalently, but without the **C**/**D** and **S**/**U**:
(note that it does not matter if you write a whitespace before or after the brackets, or both)

```
CustomerSelfServiceContext[ACL] Customer-Supplier [PL]CustomerManagementContext

```

Upstream roles are given by the [Open Host Service (OHS)](/docs/open-host-service/) and [Published Language (PL)](/docs/published-language/) patterns.
Downstream roles are [Conformist (CF)](/docs/conformist/) and [Anticorruption Layer (ACL)](/docs/anticorruption-layer/).
But have a look at the semantic rules below, to see what combinations are actually allowed.

## Semantic Rules

Note that semantic rules (validators) exist for Customer/Supplier relationships within CML. This means that not every combination of patterns and concepts is allowed, even if it would be syntactically correct.
The following rules apply to a Customer/Supplier:

* The Conformist pattern is not applicable in a Customer/Supplier relationship.
* The Open Host Service pattern is not applicable in a Customer/Supplier relationship.
* The Anticorruption Layer pattern can be used in a Customer/Supplier relationship, but this leads to contradictions with the original pattern definition according to our understanding.
  + The usage of Anticorruption Layer in a Customer/Supplier relationship produces a **Warning** only.

For a summary of all semantic rules and further justifications, please consult [Language Semantics](/docs/language-model/).

[Improve this page](https://github.com/ContextMapper/contextmapper.github.io/blob/master/_docs/language-reference/customer-supplier.md)

---

* [← Previous](/docs/shared-kernel/)
* [Next →](/docs/conformist/)

