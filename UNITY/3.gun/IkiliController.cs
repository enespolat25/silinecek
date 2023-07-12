using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class IkiliController : MonoBehaviour
{
    private Animator animator;
    // Start is called before the first frame update
    void Start()
    {
        animator = GetComponent<Animator>();

    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKey("w"))
        {
            animator.SetBool("isRunning", true);
            this.transform.Translate(new Vector3(0f, 0f, 1f) * Time.deltaTime, this.transform.parent);

        }
        else
        {
            animator.SetBool("isRunning", false);

        }

        if (Input.GetKey("s"))
        {
            animator.SetBool("isCrawling", true);
            this.transform.Translate(new Vector3(0f, 0f, 2f) * Time.deltaTime, this.transform.parent);
        }
        else
        {
            animator.SetBool("isCrawling", false);

        }

    }
}
