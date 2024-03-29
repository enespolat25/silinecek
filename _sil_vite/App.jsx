
import React from "react"
import './App.css'


function App() {
  // 1: return ederkenken HTML Yapisi Return Etmen Gerekiyor (JSX)
  // 2: return ile sadece bir parent element gonderebilirsin.. 
  // 2.1: fragment kullanilabilir <> .. </>
  // return (
  // <React.Fragment>
  //   <div>Div icindeki Bilgi</div>
  //   <h1>Merhaba</h1>
  // </React.Fragment>
  // )
  // 3: {susluParantez ici JavaScript Yapisi Calistirmak Icin Kullanilir}
  // 4: Bir Etiketin Muhakkak Bitisi Olmalidir (<etiket>..</etiket> -> <etiket /> )
  // 5: class bilgisi className diye Yazilmali..
  // 6: return icinde aciklama icin yine susluParantez Kullanilmali {/* aciklama.. */}
  // 7: style bilgisi {js icinde {obj olcak sekilde olmalidir}} -> {{backgroundColor: "yellow", listStyle: "none", margin: 0, padding: 0}}
  // 8: map kullanirken muhakkak key bilgisini gondermemiz gerekir
  // 9: React Componentlerinin Ilk Harfleri Her Zaman Buyuk Olmali.. BirdenFalzaKelimeIse..HerKelimeninIlkHarfiBuyukOlmali..
  const userName = "Derya"
  const users = ["Lorem", "Ipsum", "Dolor"]

  const products = [
    {id: 1,name: "MacBook Pro 14", inStock: false},
    {id: 2,name: "MacBook Pro 13", inStock: true},
    {id: 3,name: "iPad", inStock: false},
    {id: 4,name: "Lenovo 14", inStock: true},
    {id: 5,name: "Dell XPS", inStock: true},
  ]

  const mapUsers = users.map((item, index) => <li key={index}>{item}</li>)

  const isActive = false

  const styles = {
    h2Style: {backgroundColor: "blue", fontSize: "24px"}
  }

  return (<>
    <div className="bg-red">Div icindeki Bilgi</div>
    <h1 style={{backgroundColor: `${isActive ? "green" : "orange"}`}}>Merhaba (2 + 2 String Bilgi) {2 + 2} {userName}</h1>
    <h2 style={styles.h2Style}>Kullanicilarin Sayisi: {users.length}</h2>
    <img src="https://picsum.photos/200/300" alt="" />
    <div className="bg-red">BG Red Class ile Eklendi</div>
    {/* Bu Kullanim Dogru Degil */}
    <ul>
      <li>{users[0]}</li>
      <li>{users[1]}</li>
      <li>{users[2]}</li>
    </ul>
    {/* Dogru Kullanim v1 */}
    <ul>
      {users.map((item, index) => <li key={index}>{item}</li>)}
    </ul>

    {/* Dogru Kullanim v2 */}
    <ul style={{backgroundColor: "yellow", listStyle: "none", margin: 0, padding: 0}}>
      {mapUsers}
    </ul>

    <ul>
      {products
        .filter(item => item.inStock)
        .map(item => 
          <li key={item.id}>{item.name.toUpperCase()}</li>
        )
      }
    </ul>
    
  </>)
}



export default App