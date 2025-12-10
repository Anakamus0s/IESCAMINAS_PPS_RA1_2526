# Apartado 4 

---

Aqui se adjunta el tutorial realizado en la URL [https://cryptozombies.io/en/course](https://cryptozombies.io/en/course).
Pantallazo: 

![Pantallazo criptozombies](../../imagenes/PantallazoCripotZombies.png)

---

## Smart Contract privado 

Se ha agregado un smart contract que hace uso de un árbol de merkle llamado contrato.sol.

### Explicación del contrato:

1. Guardado del Merkle Root
El contrato almacena el valor `merkleRoot`, que representa la raíz del árbol.

2. Guarda al dueño del contrato
También guarda la dirección del dueño, que es la única persona que puede actualizar el Merkle Root.

3. Constructor
Cuando se despliega el contrato:
   - Se establece el Merkle Root inicial.
   - Se guarda la dirección quien despliega el contrato.

4. Actualizar el Merkle Root
La función `updateMerkleRoot` permite cambiar el Merkle Root, esta solo es accesible por el dueño.

5. Verificar un proof
La función `verifyProof` permite comprobar si un dato pertenece al árbol de Merkle.

