
# Domain Vision Statement

The Domain Vision Statement pattern from the [“blue book”](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215) is implemented as a String attribute on the [bounded context](/docs/bounded-context), the [domain](/docs/subdomain), and the
[subdomain](/docs/subdomain).

## Syntax

The following two code snippets show an example for a bounded context, a domain, and a subdomain accordingly:

```
BoundedContext CustomerContext {
  domainVisionStatement = "This context is responsible for ..."
}

```

```
Domain Insurance {
  domainVisionStatement = "Insurance domain vision ..."

  Subdomain Customers {
    /* subdomain specification */
  }

  Subdomain PolicyManagement {
    /* subdomain specification */
  }
}

```

```
Subdomain CustomerManagementDomain {
  type = CORE_DOMAIN
  domainVisionStatement = "Subdomain managing everything customer-related."
}

```

[Improve this page](https://github.com/ContextMapper/contextmapper.github.io/blob/master/_docs/language-reference/domain-vision-statement.md)

---

* [← Previous](/docs/subdomain/)
* [Next →](/docs/partnership/)

