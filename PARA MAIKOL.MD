Si no especifico q tipo de peticion acepta la direccion significa q acepta get, post, update y delete

los q llevan asteriscos los explico al final 

nama t voy a decir las urls finales recuerda q el ip depende del q lo montes:


urls:

user_reg/ > para crear, editar, modificar y eliminar usuarios, no he puesto los permisos pero ya sabes como va

data_transaction/ >datos internos de las transacciones.

logout/ > solo acepta get

pay/ > igual

api-auth > autenticacion, post nama

api-token-auth > autenticacion pero devuelve un token, post nadamas, en los dos pasas usuario y contrasegna

pdfs/ > * para descargar y guardar pdfs, acepta create, get 

not_reg_pdf >  * pdfs q no han sido registrado como book, devuelve dos id, uno del pdf y otro para preview.

authors/ grupd de autores,

books/ > *1 aqui para salvar necesitas extra info antes de mandarlo en la base de datos, luego t explico.

preview_pdfs/  > *los previews, al igual q pdfs.


los q tienen * significan q si le agnades al final un id t devolvera ese objeto en especifico, en otro caso t devuelve todos.

para el post de books necesitas darme dos ids de pdfs y previews, lista los not_reg_pdf y luego al dar click en uno guarda los datos para mandarlos junto al post


Hay una carpeta q se llama jsons, va incluir un ejemplo de los gets, en caso de tener q hacer un post mandame los datos con los mismos nombres de las llaves y esas cosas.

La lista de cosas q llevan post:

pdfs
authors
books
preview_pdf
data_transactions
user

Esos son los unicos datos, q espero q me mandes.
