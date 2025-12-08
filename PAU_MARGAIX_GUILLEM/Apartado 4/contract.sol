// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleMerkleChainPauMargaix {

    bytes32 public merkleRoot;
    address private owner;

    constructor(bytes32 _initialRoot) {
        merkleRoot = _initialRoot;
        owner = msg.sender; // guardamos la direccion del que actualiza el merkle root 
    }

    function updateMerkleRoot(bytes32 _newRoot) public { // funcion publica para actualizar el merkle root
        require(msg.sender == owner, "No autorizado");
        merkleRoot = _newRoot;
    }

    function verifyProof( // funcion para verificar el proof
        bytes32 leaf,
        bytes32[] memory proof
    ) public view returns (bool) {

        bytes32 computedHash = leaf;

        for (uint256 i = 0; i < proof.length; i++) { // recorremos el proof
            bytes32 proofElement = proof[i];

            if (computedHash <= proofElement) { // ordenamos los hashes
                computedHash = keccak256(
                    abi.encodePacked(computedHash, proofElement)
                );
            } else { // si no estan ordenados, los invertimos
                computedHash = keccak256(
                    abi.encodePacked(proofElement, computedHash)
                );
            }
        }

        return computedHash == merkleRoot; 
    }
}
