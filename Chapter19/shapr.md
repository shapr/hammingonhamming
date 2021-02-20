Reliability of Simulations
* How would I even measure the reliability of a simulation? Is there some feedback loop? Hamming says "No panacea, all you have is yourself"
  737 MAX simulators turned out to [be required](https://www.seattletimes.com/business/boeing-aerospace/boeing-says-all-737-max-pilots-will-need-flight-simulator-training/)
* Older minds are slower to adjust to radically new ideas.
  Ok, How do I recognize when an idea is radically new?
* [Simpson's Paradox](https://en.wikipedia.org/wiki/Simpson%27s_paradox) starts out with the 1973 UC Berkeley gender bias.
  This reminds me of [Anscomb's quartet](https://en.wikipedia.org/wiki/Anscombe%27s_quartet), where stats can give varying answers on the same data.
* Beware of any simulation where a human can alter their choices to break that simulation,
  related: [Goodhart's Law](https://en.wikipedia.org/wiki/Goodhart%27s_law) aka "When a measure becomes a target, it ceases to be a good measure." (via [Marilyn Strahern](https://en.wikipedia.org/wiki/Goodhart%27s_law#Generalization_by_Marilyn_Strathern))
* This looks like the right article for [method of scenarios](https://en.wikipedia.org/wiki/Scenario_planning) with all the same criticisms Hamming gives in this chapter.
  one example: "a prediction that cybersecurity will become a major issue may cause organizations to implement more security cybersecurity measures, thus limiting the issue"
* What's up with this seven to ten samples to stay inside the Nyquist limit? "We only get one half" is that the sideband thing opticron mentioned?
  Two samples for Nyquist, time two more samples if we have "only one side", so that's at least eight? Does Hamming add two more for a margin of error?
  * what's this "Competent designer should be able to give you the frequency content of a signal" bit?
* I think the step by step sampling of a simulation function relates directly to [Pymaxion](https://github.com/m-clare/pymaxion) ?
* Where would analog components still be useful? You could beat the [dolphin attack](https://www.bbc.com/news/technology-41188557) if nothing else?

Questions
* Maybe meta-simulations could be useful? How might the entire system (company?) react to particular simulation results?
* How do you build redundancy into a simulation?
  Perhaps you never rely on a single input for stability?
