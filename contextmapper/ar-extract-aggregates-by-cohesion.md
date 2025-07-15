
# AR-5: Extract Aggregates by Cohesion

Extracts a set of aggregates which are chosen by certain cohesion criteria and moves them to a separate bounded context.

## Context & Rationales

By decomposing a system into multiple bounded contexts we aim for loose coupling between the bounded context and a high cohesion
within them. There are many different approaches and different coupling criteria by which the software architect may want
to decompose a system into components.

**See also:**

* [Coupling criteria catalog](https://github.com/ServiceCutter/ServiceCutter/wiki/Coupling-Criteria) of [ServiceCutter](https://servicecutter.github.io/)

## Goal

This Architectural Refactoring (AR) allows to manually select the aggregates which should be extracted by any coupling criteria
or Non-functional Requirements (NFR). The goal of this AR is to isolate a set of aggregates within a new bounded context by
an individual criterion.

**Inverse AR’s:**

* [AR-7: Merge Bounded Contexts](/docs/ar-merge-bounded-contexts/)

## Preconditions

* The selected bounded context must contain **at least two aggregates**.

## Input

* One bounded context.
* A selection of aggregates which shall be extracted to a new bounded context.

## Output

* A new bounded context containing the selected aggregates.

## Example

The following example illustrates how this AR can be applied. The corresponding sources can be found in our
[examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/architectural-refactorings).

### Input

The bounded context in the example contains multiple aggregates. The AR is available on this bounded context:

[![Extract Aggregates by Cohesion Example Input](/img/extract-aggregates-by-cohesion-input.png)](/img/extract-aggregates-by-cohesion-input.png)

### Manual Selection Dialog

Once you triggered the refactoring a dialog will pop up, allowing you to choose a name for the new bounded context and the aggregates
which should be extracted:

[![Extract Aggregates by Cohesion Example Dialog](/img/extract-aggregates-by-cohesion-dialog.png)](/img/extract-aggregates-by-cohesion-dialog.png)

**Note** that if you select all Aggregates within this dialog you end up with an empty Bounded Context, since everything is
moved to a new Bounded Context. From our perspective selecting all Aggregates does therefore not make much sense. You can alternatively
simply rename the existing Bounded Context.

### Result

The resulting model contains a new bounded context with the selected aggregates:

[![Extract Aggregates by Cohesion Example Output](/img/extract-aggregates-by-cohesion-output.png)](/img/extract-aggregates-by-cohesion-output.png)

## Example Sources

* You can find the CML sources for this AR example
  [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/architectural-refactorings/AR-5-Extract-Aggregates-by-Cohesion).

[Improve this page](https://github.com/ContextMapper/contextmapper.github.io/blob/master/_docs/architectural-refactorings/ar-extract-aggregates-by-cohesion.md)

---

* [← Previous](/docs/ar-extract-aggregates-by-volatility/)
* [Next →](/docs/ar-merge-aggregates/)

