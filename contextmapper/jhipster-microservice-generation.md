
# Generate Microservices From Context Map Using JHipster

[JHipster](https://www.jhipster.tech/) is a development platform to generate [Spring Boot](https://spring.io/projects/spring-boot) web applications and microservices. Applications
or microservices, including their Entities and relationships between these Entities, can be specified with the [JHipster Domain Language (JDL)](https://www.jhipster.tech/jdl/).
The JHipster generator is able to generate code for the microservices (based on the Spring framework and several frontend frameworks) with a JDL file as input.

By providing a JDL template for our [generic generator (templating based on Freemarker)](/docs/generic-freemarker-generator/), we offer a tool to generate microservices from
your [CML Context Map](/docs/context-map/) using [JHipster](https://www.jhipster.tech/). In this tutorial we show you how you can generate microservice applications from
DDD-based models in Context Mapper.

**Note** that the current solution with the Freemarker template is only temporary. We are working on an integration of the JDL language into Context Mapper.
If you have problems using the JHipster generator with the produced JDL output please let us know and
[create a Github issue](https://github.com/ContextMapper/context-mapper-dsl/issues/new).

## The Example Model

We use our fictitious insurance example application that can be found in the [examples repository](https://github.com/ContextMapper/context-mapper-examples) to illustrate the
microservice generation with JDL and JHipster. The following graphical Context Map shows the Bounded Contexts of the system.

[![Insurance example Context Map](/img/insurance-example-for-JDL-generation_ContextMap.png)](/img/insurance-example-for-JDL-generation_ContextMap.png)

The complete CML model used for this tutorial can be found [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/microservice-generation/JDL-example).
Please note that the current JDL template only filters/ignores Bounded Contexts of the type *TEAM* when creating microservices. For all other types of Bounded Contexts
(FEATURES, APPLICATIONS, and SYSTEMS) are mapped to a corresponding microservice. Our example Context Map, shown in the following CML snippet, contains several Bounded
Contexts of the type *SYSTEM*. The generator creates one microservice per Bounded Context.

```
ContextMap InsuranceContextMap {
  type = SYSTEM_LANDSCAPE
  state = TO_BE

  contains CustomerManagement, CustomerSelfService, Printing
  contains PolicyManagement, RiskManagement, DebtCollection

  CustomerSelfService [D,C]<-[U,S] CustomerManagement {
    exposedAggregates = Customers
  }

  CustomerManagement [D,ACL]<-[U,OHS,PL] Printing {
    implementationTechnology = "SOAP"
    downstreamRights = INFLUENCER
    exposedAggregates = Printing
  }

  Printing [U,OHS,PL]->[D,ACL] PolicyManagement {
    implementationTechnology = "SOAP"
    exposedAggregates = Printing
  }

  RiskManagement [P]<->[P] PolicyManagement {
    implementationTechnology = "RabbitMQ"
  }

  PolicyManagement [D,CF]<-[U,OHS,PL] CustomerManagement {
    implementationTechnology = "RESTfulHTTP"
    exposedAggregates = Customers
  }

  DebtCollection [D,ACL]<-[U,OHS,PL] Printing {
    implementationTechnology = "SOAP"
    exposedAggregates = Printing
  }

  PolicyManagement [SK]<->[SK] DebtCollection {
    implementationTechnology = "Shared Java Library, Communication over RESTful HTTP"
  }
}

```

Each Bounded Context of the model contains Aggregates with Entities and Services. The following CML snippet (CustomerManagement) illustrates an example:

```
BoundedContext CustomerManagement implements CustomerManagementDomain {
  type = SYSTEM
  domainVisionStatement = "The customer management context is responsible for managing all the data of the insurance companies customers."
  implementationTechnology = "Java, JEE Application"
  responsibilities = "Customers, Addresses"

  Aggregate Customers {
    Entity Customer {
      aggregateRoot

      - SocialInsuranceNumber sin
      String firstname
      String lastname
      - List<Address> addresses

      def AddressId createAddress(@Address address);
      def boolean changeCustomer(String firstname, String lastname);
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
}

```

All other Bounded Context definitions and the complete model can be found [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/microservice-generation/JDL-example), as already mentioned.

*Note:* The Bounded Contexts (not of type *TEAM*) and their Entities are the objects used for the transformation to JDL. The CML relationship definitions on the Context Map are
not used for the microservice generation, since JDL does not support specifying interface details between the services. However, JHipster will generate interfaces for the
communication between the services.

*Note:* References between Entities in different Bounded Contexts are currently ignored by the generator, since the JHipster generator does not support this. You have to specify
the corresponding Entities in each Bounded Context manually (for now).

## Generate JDL with Context Mapper

Once you modeled your Bounded Contexts with the Entities, you can generate a JDL file using our [generic generator](/docs/generic-freemarker-generator/).

The Freemarker template can be downloaded [here](https://github.com/ContextMapper/context-mapper-dsl/blob/master/org.contextmapper.dsl.ui/samples/freemarker/jhipster/JDL.ftl). In Eclipse you can also import the template by [creating the example templates project](/docs/generic-freemarker-generator/#user-guide) (VS Code users please download the template manually).

You can the call the generator through the context menu of the CML editor (a more detailed documentation how to use our generators can be found [here](/docs/generators/#using-the-generators)).
The Eclipse plugin or VS Code extension will ask you to choose the Freemarker template. Select the JDL.ftl file. Context Mapper will also ask you to choose a name for the output file. In this case type a file name ending with \*.jdl.

The generator will write the output file into the `src-gen` folder:

[![JDL Output Example in VS Code](/img/vscode-jdl-output-sample.png)](/img/vscode-jdl-output-sample.png)

*Note*: Install the [JHipster IDE](https://www.jhipster.tech/jhipster-ide/) in your Eclipse or VS Code if you want to have editing support for the JDL file.

*Note*: We do not introduce the JDL language itself in this tutorial. You find the documentation of the language [here](https://www.jhipster.tech/jdl/).

## Generate the Microservices with JHipster

The JDL file generated as described above contains one microservice per Bounded Context and an [API gateway](https://www.jhipster.tech/api-gateway/). In addition, we create
*Entities* within the applications and *relationships* for the references you modeled between Entities in CML.

**Prerequisites:**

For the next steps we assume you have the following tools installed on your machine:

* Java 8+
* [JHipster generator](https://www.jhipster.tech/installation/)

**Generation Process:**

First, create a folder in your sources where you want to generate the microservices from your Context Map and change to that directory:

```
$ mkdir microservice-tutorial
$ cd microservice-tutorial/

```

You can then start the JHipster generator with the JDL file as input (adjust path the generated JDL file) by using the following command:

```
$ jhipster import-jdl ./../context-mapper-examples/src-gen/insurance-microservices.jdl

```

After the generator has done its work we can check the content of the directory to see what has been generated:

```
$ ls -l
total 28
drwxrwxr-x 7 ska ska 4096 Apr 21 11:12 CustomerManagement
drwxrwxr-x 7 ska ska 4096 Apr 21 11:12 CustomerSelfService
drwxrwxr-x 7 ska ska 4096 Apr 21 11:12 DebtCollection
drwxrwxr-x 8 ska ska 4096 Apr 21 11:13 gateway
drwxrwxr-x 7 ska ska 4096 Apr 21 11:12 PolicyManagement
drwxrwxr-x 7 ska ska 4096 Apr 21 11:12 Printing
drwxrwxr-x 7 ska ska 4096 Apr 21 11:12 RiskManagement

```

As you can see in the example above, the generator created a directory for each Bounded Context / microservice. In addition, an [API gateway](https://www.jhipster.tech/api-gateway/)
is generated into the `gateway` directory.

**Running the Application**:

To run the application with all its microservices you first have to download and run the [JHipster registry](https://www.jhipster.tech/jhipster-registry/) for the service discovery.
You have two options to run the registry:

1. Clone their repository and run it as described there: <https://github.com/jhipster/jhipster-registry>
2. Download the [latest release](https://github.com/jhipster/jhipster-registry/releases) (JAR file) and run the application with `java -jar jhipster-registry-<version>.jar`

You also find a complete documentation on the installation process on [JHipsters website](https://www.jhipster.tech/jhipster-registry/#installation).

In our case, we just downloaded the latest JAR file and run the application with the command from the [JHipsters documentation](https://www.jhipster.tech/jhipster-registry/#installation):

```
$ wget https://github.com/jhipster/jhipster-registry/releases/download/v6.1.2/jhipster-registry-6.1.2.jar
$ java -jar jhipster-registry-6.1.2.jar --spring.profiles.active=dev --spring.security.user.password=admin --jhipster.security.authentication.jwt.secret=my-secret-key-which-should-be-changed-in-production-and-be-base64-encoded --spring.cloud.config.server.composite.0.type=git --spring.cloud.config.server.composite.0.uri=https://github.com/jhipster/jhipster-registry-sample-config

```

Before you continue, check the registry is up-and-running under the given port `http://localhost:8761/` (see console output; user=admin; pw=admin):

[![JHipster Registry Screenshot](/img/jhipster-tutorial-registry-screenshot.png)](/img/jhipster-tutorial-registry-screenshot.png)

After that, we opened a terminal window for each microservice (including the gateway) and started each service with `./mvnw`:

```
$ cd CustomerManagement/
$ ./mvnw

```

```
$ cd CustomerSelfService/
$ ./mvnw

```

```
$ cd DebtCollection/
$ ./mvnw

```

```
$ cd PolicyManagement/
$ ./mvnw

```

```
$ cd Printing/
$ ./mvnw

```

```
$ cd RiskManagement/
$ ./mvnw

```

```
$ cd gateway/
$ ./mvnw

```

[![Terminal with All Services Started (Screenshot)](/img/jhipster-tutorial-all-services-started-terminal-screenshot.png)](/img/jhipster-tutorial-all-services-started-terminal-screenshot.png)

Once all services are started you should also see them in the JHipster registry:

[![JHipster Registry Screenshot With Started Services](/img/jhipster-tutorial-registry-screenshot-2.png)](/img/jhipster-tutorial-registry-screenshot-2.png)

**Access the Application**:

JHipster generates one user interface as part of the gateway application. The other microservices are accessed by the generated RESTful HTTP interfaces.
Our generator assigns the port 8080 to the gateway application. Therefore you can access the application after you started all the services on <http://localhost:8080/>:

[![Started Application](/img/jhipster-tutorial-started-application-home-screen.png)](/img/jhipster-tutorial-started-application-home-screen.png)

The generated application will include user interfaces for CRUD (create, read, update, delete) operations for all your entities:

[![UIs for All Entities](/img/jhipster-tutorial-started-application-entities.png)](/img/jhipster-tutorial-started-application-entities.png)

The JHipster generator provides many options to adjust the generated applications (changing UI framework, database, etc.). Please consult the [JHipster documentation](https://www.jhipster.tech/)
if you want to adapt the JDL file and/or the generated microservices.

That’s it. A very easy way to generate microservices from a DDD/CML Context Map, isn’t it? :)

## Known Limitations

The current solution (JDL template) comes with a few limitations that we are aware of:

* In CML you can create references from one Entity to another Entity that is contained in a different Bounded Context.
  + Unfortunately this is not possible in JDL. (would be nice if JHipster would create the Entities in both microservices automatically :)
  + For now, you have to create the Entities per Bounded Context manually and ensure that you only reference Entities within the same Bounded Context.
  + *Hint*: If you create *cross-BC-references*, they are currently completely ignored by the JDL template (the future JDL integration shall fix this automatically).
* In CML you can declare duplicate Entity names as long as they are in different Bounded Contexts. For example: multiple contexts can have an Entity of the type *Customer*.
  + JDL does not support duplicate Entity names, even if they are in different microservices.
  + *Hint*: The JDL template does currently not fix this automatically. You have to ensure that you don’t have duplicate Entity names in your CML model. Otherwise the generated
    JDL file will be invalid.
* Bidirectional references: the JHipster generator creates bidirectional relationships for all *One-To-Many* relationships in JDL. However, it does not detect that the relation
  may already be declared bidirectionally.
  + The JHipster generator will generate duplicate code which leads to compiler errors if you already specify the relation in a bidirectional way in CML/JDL (two references/relationships).
  + Currently, you have to avoid this by specifying one of the relationships only (fix it manually in JDL or CML model).
* Services not used: In CML you can specify services with its operations. The JDL language does however not support such a feature and the JHipster generator creates its own
  services.
  + The service operations declared in CML do therefore not find their way into the generated applications.
  + Maybe JHipster will support the declaration of Services in JDL in the future?
* Data type mapping: In CML it is possible to reference types that are not yet defined in the model. JDL only knows primitive types or relationships to other Entities. Thus,
  we cannot map such unknown types to JDL.
  + Such types are currently mapped to *blobs*. You can avoid this by declaring corresponding Entities in CML. The generator will then add it to the JDL file and will create a
    corresponding relationship.
  + In the future we may create Entities for this types automatically (Post-Freemarker solution).
* Potential keyword clashes: If you use keywords that are reserved in JDL (for example “microservice”) as names of the used CML objects (Bounded Contexts, Entities,
  or Entity attributes), the resulting JDL file will not compile/validate. Please avoid the usage of such JDL keywords in order to ensure that the resulting file compiles
  (instead of “microservice”, you could use “AMicroservice” or “My\_microservice”).
  + The JDL language with its keywords is documented [here](https://www.jhipster.tech/jdl/getting-started).

If you run into other problems with the generator, [let us know](https://github.com/ContextMapper/context-mapper-dsl/issues/new/).

## Frequently Asked Questions (FAQs)

* **How can I generate a monolithic application instead of microservices?**
  + You have to adjust the generated JDL file a bit: remove the *microservice* and *application* definitions (only keep the *entities* and *relationships*).
  + After you changed the JDL as described above you can use the JHipster generator to generate a monolith with all Entities (for more instructions consult the
    [JHipster documentation](https://www.jhipster.tech/)).
  + *Hint*: You can also create one *application* of the type *monolith*, so that you don’t have to answer the questions during the generation. Find the corresponding JDL
    documentation [here](https://www.jhipster.tech/jdl/applications).
  + *Hint*: You can also change our Freemarker temple (JDL.ftl) accordingly.
* **How can I change the UI framework (for example React instead of Angular) of the gateway application or other configurations?**
  + After you generated the JDL file with our template, you can adjust the *config* section of all generated *applications* in JDL.
  + For example: add `clientFramework react` to the config block.
  + Find more documentation on how to configure your applications in JDL here: <https://www.jhipster.tech/jdl/applications#available-application-options>
* **Why does the resulting JDL file not compile/validate?**
  + Please check the known limitations list above. You probably used a reserved keyword of the JDL language for CML objects. For example: If you name a Bounded Context
    “microservice”, which is a JDL keyword, the resulting JDL file will not be valid. Please avoid using such keywords (instead of “microservice”, you could use “AMicroservice” or “My\_microservice”).
    - To check whether a word is a reserved keyword in JDL, please consult [JHipster’s JDL documentation](https://www.jhipster.tech/jdl/getting-started).
  + If you respected the known limitations, followed the corresponding instructions, and it still does not compile, please create a
    [GitHub issue in our repository](https://github.com/ContextMapper/context-mapper-dsl/issues/new/).

## More Links and Resources

* [JHipster](https://www.jhipster.tech/)
* [JHipster Domain Language (JDL)](https://www.jhipster.tech/jdl/)
* [JHipster Microservices](https://www.jhipster.tech/microservices-architecture/)
* [Context Mapper: Generic Generator (Freemarker Templates)](/docs/generic-freemarker-generator/)
* [Example model used for this tutorial](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/microservice-generation/JDL-example)

[Improve this page](https://github.com/ContextMapper/contextmapper.github.io/blob/master/_docs/tutorials/jhipster-microservice-generation.md)

---

* [← Previous](/docs/event-sourcing-and-cqrs-modeling/)
* [Next →](/docs/systematic-service-decomposition/)

