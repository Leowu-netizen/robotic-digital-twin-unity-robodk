using System.Collections;
using UnityEngine;
using UnityEngine.Networking;

public class UnityBridge : MonoBehaviour
{
    private string baseUrl = "http://127.0.0.1:5000";

    void Update()
    {
        // Press 1 → Start Conveyor
        if (Input.GetKeyDown(KeyCode.Alpha1))
        {
            Debug.Log("Starting Conveyor...");
            StartCoroutine(PostRequest("/start_conveyor"));
        }

        // Press 2 → Pick & Place
        if (Input.GetKeyDown(KeyCode.Alpha2))
        {
            Debug.Log("Running Pick & Place...");
            StartCoroutine(PostRequest("/pick_place"));
        }
    }

    IEnumerator PostRequest(string endpoint)
    {
        string url = baseUrl + endpoint;

        UnityWebRequest request = new UnityWebRequest(url, "POST");
        request.uploadHandler = new UploadHandlerRaw(new byte[0]);
        request.downloadHandler = new DownloadHandlerBuffer();
        request.SetRequestHeader("Content-Type", "application/json");

        yield return request.SendWebRequest();

        if (request.result == UnityWebRequest.Result.Success)
        {
            Debug.Log("Success: " + request.downloadHandler.text);
        }
        else
        {
            Debug.LogError("Error: " + request.error);
        }
    }
}
