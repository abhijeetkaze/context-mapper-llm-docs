
# AR-4: Extract Aggregates by Volatility

Extracts all aggregates from a bounded context by a given volatility, or likelihood for change
(RARELY, NORMAL or OFTEN), and moves them to a separate context.

## Context & Rationales

By decomposing a system into multiple bounded contexts we aim for loose coupling between the bounded context and a high cohesion
within them. One approach of decomposing components is to isolate parts which are likely to change.

**See also:**

* Coupling criterion [Structural Volatility](https://github.com/ServiceCutter/ServiceCutter/wiki/CC-4-Structural-Volatility) of [ServiceCutter](https://servicecutter.github.io/)
* [On the criteria to be used in decomposing systems into modules](https://dl.acm.org/citation.cfm?id=361623) by D. L. Parnas

In the Context Mapper DSL you can specify how often an aggregate changes with the *likelihoodForChange* attribute.
See our page [aggregate documentation page](/docs/aggregate/#likelihood-for-change) for more
details.

## Goal

This Architectural Refactoring (AR) extracts all aggregates with a given volatility which is provided as input parameter
(RARELY, NORMAL or OFTEN) and moves those aggregates into a new bounded context. Thereby you are able to isolate aggregates with
a certain likelihood for change in one bounded context. This AR can be applied if your model exhibits a bounded context with
aggregates which have different likelihoods for change.

**Inverse AR’s:**

* [AR-7: Merge Bounded Contexts](/docs/ar-merge-bounded-contexts/)

## Preconditions

* The selected bounded context must contain **at least two aggregates**.
* The aggregates of the selected bounded context must have **different likelihoods for change**.

## Input

* One bounded context.

## Output

* Another bounded context containing all the aggregates with the selected volatility.

## Example

The following example illustrates how this AR can be applied. The corresponding sources can be found in our
[examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/architectural-refactorings).

### Input

The bounded context in this example contains one aggregate which changes OFTEN, whereas the other aggregates have a *likelihood for change*
of *NORMAL* (default value). The AR is available on the bounded context:

[![Extract Aggregates by Volatility Example Input](/img/extract-aggregates-by-volatility-input.png)](/img/extract-aggregates-by-volatility-input.png)

### Selection Dialog

After triggering this refactoring, a dialog pops up on which you can choose by which volatility value you want to extract:

[![Merge Bounded Contexts Example Dialog](/img/extract-aggregates-by-volatility-dialog.png)](/img/extract-aggregates-by-volatility-dialog.png)

**Note** that you can only select volatility values which at least occur once in your Bounded Context. The selection of
a value which does not occur would not extract anything.

### Result

The resulting model contains a new bounded context with the aggregate which is likely to change (OFTEN):

[![Extract Aggregates by Volatility Example Output](/img/extract-aggregates-by-volatility-output.png)](/img/extract-aggregates-by-volatility-output.png)

## Example Sources

* You can find the CML sources for this AR example
  [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/architectural-refactorings/AR-4-Extract-Aggregates-by-Volatility).

[Improve this page](https://github.com/ContextMapper/contextmapper.github.io/blob/master/_docs/architectural-refactorings/ar-extract-aggregates-by-volatility.md)

---

* [← Previous](/docs/ar-split-bounded-context-by-owners/)
* [Next →](/docs/ar-extract-aggregates-by-cohesion/)

