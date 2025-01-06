using WebApp.Client.Pages;
using WebApp.Components;

// Azure blob usings:
using Azure.Storage.Blobs;
using Azure.Storage.Blobs.Models;
using System;
using System.IO;
using Azure.Identity;
using WebApp.Components.Services;
using Microsoft.AspNetCore.Http.Features;
using Microsoft.JSInterop;



var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorComponents()
    .AddInteractiveServerComponents()
    .AddInteractiveWebAssemblyComponents();

var configuration = builder.Configuration;

builder.Services.AddHttpClient("RAGClient", client =>
{
    client.BaseAddress = new Uri(configuration["HttpClientSettings:BaseUrl"]);
});

builder.Services.AddSingleton<MyRAGService>();
builder.Services.AddScoped<ChatStateService>(); 
builder.Services.AddScoped<BlobService>();

builder.Services.Configure<FormOptions>(options =>
{
    options.MultipartBodyLengthLimit = 10 * 1024 * 1024; // 10 MB
});

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseWebAssemblyDebugging();
}
else
{
    app.UseExceptionHandler("/Error", createScopeForErrors: true);
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();

app.UseStaticFiles();
app.UseAntiforgery();

// configure services
// for enabling the
//  - Interactive Server,
//  - Interactive WebAssembly,
//  - Interactive Auto
// render modes:
app.MapRazorComponents<App>()
    .AddInteractiveServerRenderMode()
    .AddInteractiveWebAssemblyRenderMode()
    .AddAdditionalAssemblies(typeof(Counter).Assembly);


app.Run();
