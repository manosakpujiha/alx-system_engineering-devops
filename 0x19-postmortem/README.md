Issue Summary:
On May 5th, 2023, from 2:00 PM to 4:00 PM (EST), our web application experienced a partial outage, impacting approximately 60% of our users. Users were unable to access the login page, and those already logged in experienced slow page load times and intermittent errors.

Timeline:

2:00 PM: The issue was detected through an influx of customer complaints to our support team.
2:05 PM: Our monitoring system alerted us to a spike in server errors.
2:10 PM: The operations team initiated investigations into the server logs and identified a possible issue with the load balancer.
2:30 PM: The development team was engaged to investigate the codebase and check for any issues that might have caused the load balancer to malfunction.
3:00 PM: The development team identified a recent code change that inadvertently introduced a bug, causing the load balancer to misbehave.
3:15 PM: The development team rolled back the recent code change.
3:45 PM: The load balancer was back to normal, and the issue was resolved.
Root Cause and Resolution:
The root cause of the issue was a recent code change that introduced a bug, causing the load balancer to malfunction. Specifically, the bug caused the load balancer to route traffic to a non-existent server, resulting in server errors and slow page load times.

To resolve the issue, the development team rolled back the recent code change. This action removed the bug that was causing the load balancer to malfunction and allowed traffic to be properly distributed across the server cluster.

Corrective and Preventative Measures:
To prevent similar issues from occurring in the future, the following measures will be implemented:

Automated tests will be added to the CI/CD pipeline to ensure that changes don't break the load balancer functionality.
Additional monitoring checks will be implemented to alert the operations team of similar issues before users are impacted.
A more robust error handling and logging system will be implemented to make it easier to identify and resolve issues.
Tasks to address the issue:

Add automated tests to the CI/CD pipeline to test load balancer functionality.
Implement additional monitoring checks to alert the operations team of similar issues before users are impacted.
Implement a more robust error handling and logging system to make it easier to identify and resolve issues.
Improve communication channels between teams to ensure faster and more effective incident response.
In conclusion, the partial outage that occurred on May 5th, 2023, was caused by a recent code change that introduced a bug into the system, resulting in the load balancer malfunctioning. The issue was detected through an influx of customer complaints and server error alerts, and the development team rolled back the recent code change to resolve the issue. To prevent similar issues from occurring in the future, corrective and preventative measures will be implemented, including adding automated tests, implementing additional monitoring checks, and improving communication channels between teams.

