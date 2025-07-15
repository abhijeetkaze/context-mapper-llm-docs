
# Tactic DDD Syntax

The Context Mapper syntax for the tactic DDD part is based on the [Sculptor DSL](https://sculptor.github.io/). For this reason we do not document all details of the tactic language part, since all the information can be found in Sculptor’s [documentation](https://sculptor.github.io/documentation/advanced-tutorial).
However, we still provide a short introduction into the most important elements on this page.

## Aggregates

The stategic DDD’s [bounded contexts](/docs/bounded-context) typically contain multiple aggregates. Within the aggregates, you can model
your system with the tactic DDD patterns, such as *Entity*, *Value Object*, *Domain Event*, *Service* and *Repository*.

The page [Aggregate](/docs/aggregate) describes how you can create aggregates. The following sections introduce the other patterns syntax
briefly. All of those language elements can be used within the aggregate.

## Entity

An entity is declared with the *Entity* keyword, as illustrated below. With the optional keyword *aggregateRoot* you can specify which entity
within your aggregate is the root entity. The language provides primitive data types such as *String*, *int* and *boolean* etc., similar to
Java. You can further use the collection types *List*, *Set* and *Bag*.

```
Entity Customer {
  aggregateRoot

  SocialInsuranceNumber sin
  String firstname
  String lastname
  List<Address> addresses
}

```

As illustrated in the example above, you can declare your own types (such as *Address* and *SocialInsuranceNumber* above). These types don’t
have to be further specified anywhere. However, you can also use references to existing types (entities, value objects, etc.) as described
below.

### Type References

To reference another type of your model within an attribute, you have to use the **-** (minus) sign:

```
Aggregate Customers {
  Entity Customer {
    aggregateRoot

    - SocialInsuranceNumber sin // Reference syntax for simple attribute
    String firstname
    String lastname
    - List<Address> addresses // Reference syntax for collections
  }

  Entity Address {
    String street
    int postalCode
    String city
  }

  ValueObject SocialInsuranceNumber {
    String sin key
  }
}

```

When you use this reference notation with the *-* (minus) sign, the language checks that the types (*Address* and *SocialInsuranceNumber*
above) are declared.

### Operations / Methods

Of course you can also declare methods/operations on your *Entities*, *Value Objects* and *Domain Events*. The declaration of methods
is started with the **def** keyword. As illustrated below, you can use abstract data types which are not further declared in your
method parameters and return types:

```
Entity Customer {
  aggregateRoot

  - SocialInsuranceNumber sin
  String firstname
  String lastname
  - List<Address> addresses

  def AddressId createAddress(Address address);
  def void changeCustomer(Customer customer, Address address);
}

```

If you want to **refer** existing types in your operation/method parameters and return types, you have to use the **@** character:

```
Aggregate Customers {
  Entity Customer {
    aggregateRoot

    - SocialInsuranceNumber sin
    String firstname
    String lastname
    - List<Address> addresses

    def @AddressId createAddress(@Address address); // Method/Operation declaration with references
    def void changeCustomer(@Customer customer, @Address address); // Method/Operation declaration with references
  }

  Entity Address {
    String street
    int postalCode
    String city
  }

  ValueObject SocialInsuranceNumber {
    String sin key
  }

  ValueObject AddressId {
    int id
  }
}

```

## Value Objects

The declaration of value objects is done with the *ValueObject* keyword:

```
ValueObject HandlingHistory {
  - List<HandlingEvent> handlingEvents
}

```

### Attributes & Methods/Operations

Attributes (incl. type references) and methods/operations in value objects can be specified exactly the same way as within entities (see sections above).

## Domain Events

The declaration of domain events is done with the *DomainEvent* keyword: (alternatively you can use the keyword *Event*)

```
DomainEvent HandlingEvent {
  Type handlingType;
  - Voyage voyage;
  - LocationShared location;
  Date completionTime;
  Date registrationTime;
  - Cargo cargo;
}

```

## Commands

The declaration of commands is done with the *Command* keyword: (alternatively you can use the original Sculptor keyword *CommandEvent*)

```
Command RejectClaim {
  - Claim claim2Reject
  - Employee decisionMaker
  String reason4Rejection
}

```

### Attributes & Methods/Operations

Attributes (incl. type references) and methods/operations in domain events can be specified exactly the same way as within entities (see sections above).

## Services

Within your [bounded context](/docs/bounded-context) (or also inside aggregates) you can specify domain services according to the tactic DDD *Service* pattern. Domain services are declared with the *Service* keyword and contain one or more methods/operations. These methods/operations are declared exactly the same way as within entities, value
objects or domain events, **but without the *def* keyword**:

```
Service RoutingService {
  List<@Itinerary> fetchRoutesForSpecification(@RouteSpecification routeSpecification) throws LocationNotFoundException;
}

```

With the *throws* keyword you can specify that the method/operation can throw a specific exception (as in Java).

**Note:** The [MDSL generator](/docs/mdsl/) currently only makes use of domain services that are declared inside aggregates that are [exposed in your Context Map](/docs/context-map/#exposed-aggregates).

## Repositories

You can specify a repository with the *Repository* keyword **within your aggregate root**. Only aggregate roots can contain repositories,
which is ensured by a semantic checker of the language. A repository can contain one or more methods/operations, as illustrated in
the example below. These methods/operations are declared exactly the same way as within entities, value objects or domain events,
**but without the *def* keyword**:

```
Aggregate Location {
  Entity Location {
    aggregateRoot

    PortCode portcode
    - UnLocode unLocode;
    String name;

    Repository LocationRepository {
      @Location find(@UnLocode unLocode);
      List<@Location> findAll();
    }
  }

  ValueObject UnLocode {
    String unLocode
  }

  ValueObject LocationShared {
    PortCode portCode
    - Location location
  }
}

```

## More Details about the Tactic DDD Syntax

If you want to read more details about the syntax of the tactic DDD part within bounded contexts, we refer to the [Sculptor documentation](https://sculptor.github.io/documentation/advanced-tutorial).

[Improve this page](https://github.com/ContextMapper/contextmapper.github.io/blob/master/_docs/language-reference/tactic-ddd.md)

---

* [← Previous](/docs/aggregate/)
* [Next →](/docs/application-and-process-layer/)

