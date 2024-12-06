{
  description = "A command-line tool for generating Linux commands based on user queries.";

  inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs, ... }@inputs: 
  let
      forAllSystems = nixpkgs.lib.genAttrs nixpkgs.lib.systems.flakeExposed;
      
      nixpkgsFor = forAllSystems (system: import nixpkgs { inherit system; });

      packages = forAllSystems (system: { default = import ./default.nix { pkgs = nixpkgsFor.${system}; }; });
  in {
    inherit packages;
  };

      
}