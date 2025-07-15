
# Knowledge Level

The Knowledge Level pattern can be used on bounded contexts and aggregates to specify their knowledge level, which can be one of the following values:

* CONCRETE
* META

## Syntax

The following examples show how you can specify the knowledge level on a bounded context and on an aggregate:

```
BoundedContext CustomerManagementContext implements CustomerManagementDomain {
  type = FEATURE
  domainVisionStatement = "The customer management context is responsible for ..."
  implementationTechnology = "Java, JEE Application"
  knowledgeLevel = CONCRETE
}

```

```
Aggregate Customers {
  responsibilities = Customers, Addresses { "Address description ..." }
  knowledgeLevel = CONCRETE

  Entity Customer {
    aggregateRoot

    - SocialInsuranceNumber sin
    String firstname
    String lastname
    - List<Address> addresses
  }
}

```

[Improve this page](https://github.com/ContextMapper/contextmapper.github.io/blob/master/_docs/language-reference/knowledge-level.md)

---

* [← Previous](/docs/responsibility-layers/)
* [Next →](/docs/aggregate/)

