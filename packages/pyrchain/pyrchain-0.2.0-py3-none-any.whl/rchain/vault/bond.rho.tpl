new retCh, PoSCh, rl(`rho:registry:lookup`), stdout(`rho:io:stdout`) in {
  stdout!("About to lookup pos contract.") |
  rl!(`rho:rchain:pos`, *PoSCh) |
  for(@(_, PoS) <- PoSCh) {
    stdout!("About to bond") |
    @PoS!("bond", $amount, *retCh) |
    for ( @(_, message) <- retCh) {
      stdout!(message)
    }
  }
}