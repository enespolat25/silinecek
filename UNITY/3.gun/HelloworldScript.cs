using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class HelloworldScript : MonoBehaviour
{
    public GameObject nameField;
    public GameObject popupPanel;
    public TMP_Text messageText;
    // Start is called before the first frame update
    void Start()
    {
        hidePopUpPanel();


    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void showPopUpPanel()
    {
        popupPanel.SetActive(true);
    }

    public void hidePopUpPanel()
    {
        popupPanel.SetActive(false);
        nameField.GetComponent<TMP_InputField>().text = "";
    }

    public void merhabaDe()
    {
        messageText.text = "Merhaba " + nameField.GetComponent<TMP_InputField>().text + " !";
        showPopUpPanel();
    }
}
