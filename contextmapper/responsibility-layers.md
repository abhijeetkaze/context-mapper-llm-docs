
# Responsibility Layers

The Responsibility Layers pattern from the [“blue book”](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215) can be used on bounded contexts and aggregates to specify their responsibilities.

## Syntax

The responsibilities can simply be defined with the keyword/attribute *responsibilities* and a list of responsibilities (as strings):

```
BoundedContext CustomerManagementContext implements CustomerManagementDomain {
  type = FEATURE
  domainVisionStatement = "The customer management context is responsible for ..."
  implementationTechnology = "Java, JEE Application"
  responsibilities = "Customers", "Addresses"
}

```

```
Aggregate Customers {
  responsibilities = "Customers", "Addresses"

  Entity Customer {
    aggregateRoot

    - SocialInsuranceNumber sin
    String firstname
    String lastname
    - List<Address> addresses
  }
}

```

[Improve this page](https://github.com/ContextMapper/contextmapper.github.io/blob/master/_docs/language-reference/responsibility-layers.md)

---

* [← Previous](/docs/published-language/)
* [Next →](/docs/knowledge-level/)

